# -*- coding: utf-8 -*-
"""重建银行流水 PDF：剔除「需隐藏」的转家人往来（>1000 元），余额列按转账从未发生重算。
用法: python rebuild_pdfs.py            # 解析+重建
      python rebuild_pdfs.py --parse     # 只解析打印核对
"""
import os, re, sys, json
import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))

CMB = os.path.join(HERE, '招商银行交易流水(申请时间2026年08月08日13时37分04秒).pdf')
CIT = os.path.join(HERE, 'lszm4fd0bbe26a3a4d508e663036993ee334.pdf')

HIDDEN_ACCOUNTS = ['6217002960112547937', '6221805550000575446']
HIDE_MIN = 1000.0  # 严格 > 1000 才隐藏（与 SKILL 规则一致）

DATE_RE = {
    'cmb': re.compile(r'^\d{4}-\d{2}-\d{2}$'),   # 招商: 2025-01-11
    'cit': re.compile(r'^\d{8}$'),                # 中信: 20250101
}
DATE_X_MAX = {'cmb': 60, 'cit': 30}
# 各来源的列定义：(列名, 页眉词 x0)。列边界取相邻页眉 x0 的中点，抗左对齐/右对齐差异。
HEADERS = {
    'cmb': [('date', 36), ('cur', 99), ('amount', 156), ('balance', 235),
            ('summary', 308), ('party', 418)],
    'cit': [('date', 21), ('income', 93), ('expense', 157), ('balance', 222),
            ('summary', 292), ('acct', 401), ('name', 511)],
}
PAGE_NO_RE = {'cmb': re.compile(r'^\d/3$'), 'cit': re.compile(r'^第\d页/共\d页$')}

# 页脚锚点：命中即视为页脚起点，数据带不包含其下方字
FOOTER_PATTERNS = {
    'cmb': [r'^\d/3$', r'温馨提示', r'交易流水验真', r'在线服务', r'提交系统验真',
            r'进入一网通', r'正确录入', r'^—+$'],
    'cit': [r'^第\d页/共\d页$', r'声明', r'Statement', r'本交易流水证明', r'不能流通',
            r'不能用于质押', r'不能挂失', r'请前往中信银行', r'证明用途', r'验证码',
            r'扫描二维码', r'The journal certificate', r'Please verify'],
}
NUM_RE = re.compile(r'^[-\d][\d,]*\.\d{2}$')


def make_classifier(kind):
    """按页眉 x0 中点生成列边界，返回 (boundaries, cols)：x < b[0] 归第一列…"""
    hdrs = HEADERS[kind]
    bounds = []
    for i in range(len(hdrs) - 1):
        bounds.append((hdrs[i][1] + hdrs[i + 1][1]) / 2.0)
    cols = [h[0] for h in hdrs]
    return bounds, cols


def classify(band, kind):
    bounds, cols = make_classifier(kind)
    num_cols = {'cur', 'amount', 'balance', 'income', 'expense'}
    cells = {c: [] for c in cols}
    for w in band:
        t, x0 = w['text'], w['x0']
        # 找 x0 落在哪个列区间
        ci = 0
        for b in bounds:
            if x0 < b:
                break
            ci += 1
        col = cols[min(ci, len(cols) - 1)]
        if NUM_RE.match(t):
            cells[col].append(t)          # 金额/余额数字
        elif col not in num_cols:
            cells[col].append(t)          # 文本列（摘要/对手/账号/户名）
    # 文本列拼接；金额列取最右（同一列内可能有多余数字，取最后一个）
    d = {}
    for c in cols:
        if c in ('summary', 'party', 'acct', 'name'):
            d[c] = ' '.join(cells[c])
        elif c in ('amount', 'balance', 'income', 'expense'):
            d[c] = cells[c][-1] if cells[c] else ''
        else:
            d[c] = cells[c][-1] if cells[c] else ''
    return d


def parse(fn, kind):
    dre, dmax, pnre = DATE_RE[kind], DATE_X_MAX[kind], PAGE_NO_RE[kind]
    footer_pats = [re.compile(p) for p in FOOTER_PATTERNS[kind]]
    rows = []  # (page, row_dict)
    with pdfplumber.open(fn) as pdf:
        for pno, page in enumerate(pdf.pages, 1):
            words = page.extract_words(use_text_flow=False)
            # 页脚起始 y：首个命中页脚锚点的词
            footer_y = page.height
            for w in words:
                if any(p.match(w['text']) for p in footer_pats):
                    footer_y = min(footer_y, w['top'])
            data_words = [w for w in words if w['top'] < footer_y]
            # 数据行起始：日期词在左列
            starts = []
            for w in data_words:
                if w['x0'] < dmax and dre.match(w['text']):
                    starts.append((w['top'], w))
            starts.sort()
            for i, (ys, w0) in enumerate(starts):
                # 相邻日期行中点切分竖带：跨行附言片段（常落带间）归到更近的一笔
                lo = (starts[i - 1][0] + ys) / 2 if i > 0 else max(0.0, ys - 20)
                hi = (ys + starts[i + 1][0]) / 2 if i + 1 < len(starts) else footer_y
                band = [w for w in data_words if lo <= w['top'] < hi]
                r = classify(band, kind)
                r['date'] = w0['text']
                rows.append((pno, r))
    return rows


def is_hidden(r, kind):
    acct_txt = ' '.join([r.get('party', ''), r.get('acct', ''), r.get('name', ''),
                         r.get('summary', '')])
    acct_hit = any(a in acct_txt for a in HIDDEN_ACCOUNTS)
    if not acct_hit:
        return False
    amt = r.get('amount') or r.get('expense') or r.get('income') or ''
    try:
        v = float(amt.replace(',', ''))
    except (ValueError, AttributeError):
        return False
    return abs(v) > HIDE_MIN


def recompute(rows, kind, hidden_idx):
    """保留非隐藏行，重算余额。返回 (保留行列表)。"""
    kept = []
    prev = None
    for i, (pno, r) in enumerate(rows):
        if i in hidden_idx:
            continue
        r = dict(r)
        if kind == 'cmb':
            delta = float(r['amount'].replace(',', '')) if r['amount'] else 0.0
            if prev is None:
                prev = float(r['balance'].replace(',', ''))
            else:
                prev = round(prev + delta, 2)
            r['balance_new'] = f'{prev:,.2f}'
        else:
            inc = float(r['income'].replace(',', '')) if r['income'] else 0.0
            exp = float(r['expense'].replace(',', '')) if r['expense'] else 0.0
            if prev is None:
                prev = float(r['balance'].replace(',', ''))
            else:
                prev = round(prev + inc - exp, 2)
            r['balance_new'] = f'{prev:,.2f}'
        kept.append((pno, r))
    return kept


# ================================================================ reportlab 重建
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, Paragraph,
                                Spacer)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

FONT = 'SimSun'
FONT_PATH = r'C:\Windows\Fonts\simsun.ttc'
_R_FONT = False


def _reg_font():
    global _R_FONT
    if not _R_FONT:
        pdfmetrics.registerFont(TTFont(FONT, FONT_PATH, subfontIndex=0))
        _R_FONT = True


def _ps(name, size=9, align=0, bold=False, leading=None, space=0):
    return ParagraphStyle(name, fontName=FONT, fontSize=size,
                          alignment=align, leading=leading or (size * 1.3),
                          spaceAfter=space, textColor=colors.black)


def clean_name_account(s):
    """把「名 称 数字账号」整理为 (名称, 账号)：名称间空格去掉，账号独立。"""
    s = (s or '').strip()
    if not s:
        return '', ''
    m = re.search(r'(\d{6,})\s*$', s)
    if m:
        return s[:m.start()].replace(' ', ''), m.group(1)
    return s.replace(' ', ''), ''


def build(out_fn, kind, kept):
    _reg_font()
    PW, PH = A4
    ML = 36  # 左边界，与原件一致
    doc = SimpleDocTemplate(out_fn, pagesize=A4,
                            leftMargin=ML, rightMargin=36,
                            topMargin=36, bottomMargin=52,
                            title=('招商银行交易流水（隐藏版）' if kind == 'cmb'
                                   else '账户交易明细（隐藏版）'))
    story = []
    title = _ps('t', 15, align=1, bold=True, space=6)
    sub = _ps('s', 9, align=1, space=4)
    meta = _ps('m', 9, space=2)
    meta2 = _ps('m2', 9, space=2)

    if kind == 'cmb':
        story.append(Paragraph('招商银行交易流水', title))
        story.append(Paragraph('Transaction Statement of China Merchants Bank', sub))
        story.append(Paragraph('2025-01-01 -- 2025-12-31', sub))
        story.append(Paragraph('户 名：聂庭阳    账号：6214832030228642', meta))
        story.append(Paragraph('账户类型：ALL/全币种    开 户 行：广州番禺奥园广场支行', meta))
        story.append(Paragraph('申请时间：2026-08-08 13:37:04', meta2))
    else:
        story.append(Paragraph('账户交易明细', title))
        story.append(Paragraph('Transaction details', sub))
        story.append(Paragraph('户名：聂庭阳    证件类型：居民身份证    证件号码：430528198911130018', meta))
        story.append(Paragraph('账号：6217680910778096    时间段：20250101-20251231    开立日期：2026-08-08', meta))
        story.append(Paragraph('查询最低限额：0    币种：全部', meta2))
    story.append(Spacer(1, 8))

    th = _ps('th', 9, bold=True, align=1)
    td_l = _ps('l', 9)
    td_r = _ps('r', 9, align=2)

    if kind == 'cmb':
        widths = [58, 48, 80, 80, 118, 139]  # 合计 523
        head = ['记账日期', '货币', '交易金额', '联机余额', '交易摘要', '对手信息']
        body = [head]
        for pno, r in kept:
            name, acct = clean_name_account(r.get('party', ''))
            party = (name + (' ' + acct if acct else '')).strip()
            body.append([Paragraph(r['date'], td_l),
                         Paragraph(r.get('cur', '') or 'CNY', td_l),
                         Paragraph(r['amount'], td_r),
                         Paragraph(r['balance_new'], td_r),
                         Paragraph(r.get('summary', ''), td_l),
                         Paragraph(party, td_l)])
    else:
        widths = [42, 66, 66, 68, 96, 108, 77]  # 合计 523
        head = ['交易日期', '收入金额', '支出金额', '账户余额', '交易摘要', '对方账号', '对方户名']
        body = [head]
        for pno, r in kept:
            name = r.get('name', '').replace(' ', '')
            body.append([Paragraph(r['date'], td_l),
                         Paragraph(r.get('income', ''), td_r),
                         Paragraph(r.get('expense', ''), td_r),
                         Paragraph(r['balance_new'], td_r),
                         Paragraph(r.get('summary', ''), td_l),
                         Paragraph(r.get('acct', ''), td_l),
                         Paragraph(name, td_l)])

    tbl = Table(body, colWidths=widths, repeatRows=1)
    tbl.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), FONT),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EEEEEE')),
        ('FONTNAME', (0, 1), (-1, -1), FONT),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#C8C8C8')),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, colors.black),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(tbl)

    # 末页落款
    if kind == 'cmb':
        story.append(Spacer(1, 14))
        note = _ps('note', 8, leading=12)
        story.append(Paragraph('温馨提示：', note))
        story.append(Paragraph('1.本交易流水已按约定剔除部分转家人往来记录，余额已相应重算；'
                               '如需原始版本请使用原 PDF 文件。', note))
    else:
        story.append(Spacer(1, 14))
        note = _ps('note', 8, leading=12)
        story.append(Paragraph('声明：', note))
        story.append(Paragraph('本交易流水证明不能流通，不能用于质押，不能挂失', note))
        story.append(Paragraph('The journal certificate of this transaction cannot be '
                               'circulated, used for pledge or reported for loss.', note))
        story.append(Spacer(1, 6))
        story.append(Paragraph('证明用途：申请签证', note))
        story.append(Paragraph('Certificate purpose', note))

    def _page_bg(cv, doc_):
        pass

    def _footer(cv, doc_):
        cv.saveState()
        cv.setFont(FONT, 8)
        cv.setFillColor(colors.black)
        cv.drawString(PW / 2 - 10, 24, str(doc_.page))
        cv.restoreState()

    doc.build(story, onFirstPage=_footer, onLaterPages=_footer)
    return out_fn


def main():
    only_parse = '--parse' in sys.argv
    out_names = {'cmb': '招商银行交易流水_隐藏版.pdf', 'cit': 'lszm4fd0bbe26a3a4d508e663036993ee334_隐藏版.pdf'}
    for fn, kind, label in [(CMB, 'cmb', '招商'), (CIT, 'cit', '中信')]:
        rows = parse(fn, kind)
        hidden = {i for i, (_, r) in enumerate(rows) if is_hidden(r, kind)}
        kept = recompute(rows, kind, hidden)
        print(f'\n===== {label} PDF =====  total={len(rows)} hidden={len(hidden)} kept={len(kept)}')
        if only_parse:
            for i, (pno, r) in enumerate(rows):
                tag = ' HIDE' if i in hidden else '     '
                if kind == 'cmb':
                    print(f'{tag} {pno} {r["date"]}  {r["amount"]:>12}  {r["balance"]:>12}  '
                          f'{r["summary"]}  {r["party"]}')
                else:
                    print(f'{tag} {pno} {r["date"]}  in={r["income"]:>10}  out={r["expense"]:>10}  '
                          f'bal={r["balance"]:>10}  {r["summary"]}  {r["acct"]}  {r["name"]}')
        else:
            out = os.path.join(HERE, out_names[kind])
            build(out, kind, kept)
            print(f'  输出 → {out}')


if __name__ == '__main__':
    main()
