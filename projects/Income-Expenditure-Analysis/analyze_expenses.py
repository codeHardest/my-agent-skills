# -*- coding: utf-8 -*-
"""
2025 年度流水支出分析：去重 + 按类别统计
输入: 微信支付流水.xlsx / 支付宝交易明细.csv / 中信银行流水.pdf / 招商银行流水.pdf
输出: output/支出分析.xlsx / 支出分析.md / charts/*.png
"""
import os, re, csv, base64
import pandas as pd
import pdfplumber

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'output')
CHART_DIR = os.path.join(OUT, 'charts')
os.makedirs(CHART_DIR, exist_ok=True)

WECHAT_XLSX = os.path.join(HERE, '微信支付账单流水文件(20250101-20251231)_20260809131636.xlsx')
ALIPAY_CSV  = os.path.join(HERE, '支付宝交易明细(20250101-20251231).csv')
CITIC_PDF   = os.path.join(HERE, 'lszm4fd0bbe26a3a4d508e663036993ee334.pdf')
CMB_PDF     = os.path.join(HERE, '招商银行交易流水(申请时间2026年08月08日13时37分04秒).pdf')


def money(s):
    try:
        return float(str(s).replace(',', ''))
    except Exception:
        return 0.0


# ---------------------------------------------------------------- 解析
def parse_wechat():
    df = pd.read_excel(WECHAT_XLSX, header=17)
    df.columns = ['交易时间', '交易类型', '交易对方', '商品', '收支', '金额',
                  '支付方式', '当前状态', '交易单号', '商户单号', '备注']
    df = df[df['交易时间'].notna()].copy()
    df['金额'] = pd.to_numeric(df['金额'], errors='coerce')
    df['日期'] = pd.to_datetime(df['交易时间'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['来源'] = '微信'
    return df


def parse_alipay():
    with open(ALIPAY_CSV, encoding='gbk') as f:
        rows = list(csv.reader(f))
    # 表头在第 23 行（0 基索引），截断末尾空列
    data = [r[:12] for r in rows[24:] if r and r[0].strip() and r[5].strip()]
    df = pd.DataFrame(data, columns=['交易时间', '交易分类', '交易对方', '对方账号', '商品说明',
                                     '收支', '金额', '付款方式', '交易状态', '订单号', '商家单号', '备注'])
    df['金额'] = pd.to_numeric(df['金额'], errors='coerce')
    df['日期'] = pd.to_datetime(df['交易时间'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['来源'] = '支付宝'
    return df


def alipay_refunds(df):
    """返回支付宝退款行（不计收支中含「退款」的行），金额取正，并映射回原订单类别。"""
    nb = df[df['收支'] == '不计收支']
    refund = nb[nb['商品说明'].str.contains('退款', na=False)].copy()
    if refund.empty:
        return refund
    exp = df[df['收支'] == '支出'].copy()
    exp['mid'] = exp['商家单号'].str.strip()
    exp['cat'] = exp.apply(map_alipay, axis=1)
    mid_to_cat = {}
    for mid, cat in zip(exp['mid'], exp['cat']):
        if mid:
            mid_to_cat.setdefault(mid, cat)
    refund['mid'] = refund['商家单号'].str.strip()
    refund['类别'] = refund['mid'].map(mid_to_cat).fillna(
        refund.apply(map_alipay, axis=1))
    refund['金额'] = refund['金额'].abs()
    return refund


AMT_RE = re.compile(r'^[\d,]+\.\d{2}$')


def _word_groups(pdf_path):
    """把 PDF 每页按 y 聚类成行，非日期行(对方户名折行)合并到上一行。返回行词列表。"""
    groups = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            lines = {}
            for w in page.extract_words():
                lines.setdefault(round(w['top'] / 4), []).append(w)
            cur = []
            for key in sorted(lines):
                ws = sorted(lines[key], key=lambda w: w['x0'])
                # 新行: 行首是日期
                is_date = bool(ws and ws[0]['x0'] < 120 and
                               (re.match(r'^\d{8}$', ws[0]['text']) or re.match(r'^\d{4}-\d{2}-\d{2}$', ws[0]['text'])))
                if is_date:
                    if cur:
                        groups.append(cur)
                    cur = ws
                else:
                    if cur:
                        cur.extend(ws)
                    else:
                        cur = ws
            if cur:
                groups.append(cur)
    return groups


def parse_citic():
    rows = []
    for ws in _word_groups(CITIC_PDF):
        ws = sorted(ws, key=lambda w: w['x0'])
        date = ws[0]['text'] if ws else ''
        if not re.match(r'^\d{8}$', date):
            continue
        def col(x):
            if x < 90:   return 0
            if x < 157:  return 1
            if x < 222:  return 2
            if x < 300:  return 3
            return 4
        cells = {}
        for w in ws:
            cells.setdefault(col(w['x0']), []).append(w)
        def pick(c):
            return ''.join(x['text'] for x in cells.get(c, []) if AMT_RE.match(x['text']))
        # 明细: 摘要/账号/户名（非金额词，x>=265 起）
        detail = ''.join(w['text'] for w in ws
                         if w['x0'] >= 265 and not AMT_RE.match(w['text']))
        rows.append({
            '日期': f"{date[:4]}-{date[4:6]}-{date[6:]}",
            '收入': money(pick(1)),
            '支出': money(pick(2)),
            '余额': money(pick(3)),
            '明细': detail,
        })
    return rows


def parse_cmb():
    rows = []
    for ws in _word_groups(CMB_PDF):
        ws = sorted(ws, key=lambda w: w['x0'])
        date = ws[0]['text'] if ws else ''
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
            continue
        amt = None
        for w in ws:
            if re.match(r'^-?[\d,]+\.\d{2}$', w['text']):
                amt = money(w['text'])
                break
        if amt is None:
            continue
        # 明细: 去掉日期/CNY/金额/余额后的其余词（摘要+对方户名）
        skip = {w['text'] for w in ws if re.match(r'^\d{4}-\d{2}-\d{2}$', w['text']) or
                w['text'] in ('CNY', 'RMB') or re.match(r'^-?[\d,]+\.\d{2}$', w['text'])}
        detail = ''.join(w['text'] for w in ws if w['text'] not in skip)
        rows.append({'日期': date, '金额': amt, '明细': detail})
    return rows


# ---------------------------------------------------------------- 类别
# 统一类别集（支付宝 19 类 + 网购/平台、现金；另立: 转账往来、储蓄投资、内部转账）
CONSUME_CATS = ['餐饮美食', '日用百货', '交通出行', '文化休闲', '充值缴费', '医疗健康',
                '家居家装', '生活服务', '商业服务', '服饰装扮', '住房物业', '美容美发',
                '母婴亲子', '运动户外', '教育培训', '酒店旅游', '爱车养车', '网购/平台', '现金', '其他']
ALIPAY_CAT_MAP = {
    '日用百货': '日用百货', '餐饮美食': '餐饮美食', '交通出行': '交通出行', '文化休闲': '文化休闲',
    '充值缴费': '充值缴费', '医疗健康': '医疗健康', '家居家装': '家居家装', '其他': '其他',
    '生活服务': '生活服务', '商业服务': '商业服务', '服饰装扮': '服饰装扮', '住房物业': '住房物业',
    '美容美发': '美容美发', '母婴亲子': '母婴亲子', '运动户外': '运动户外', '教育培训': '教育培训',
    '酒店旅游': '酒店旅游', '爱车养车': '爱车养车',
    '信用借还': '转账往来',
}

# 微信商户关键词规则（按顺序匹配）→ (类别, 关键词列表)
WECHAT_RULES = [
    ('交通出行', ['滴滴', '出租', '铁路', '高速', '联合电子', '地铁', '公交', '岭南通', '粤通卡', '12306', '航空', '飞机',
                  '停车场', '西站', '驿站取货']),
    ('充值缴费', ['国家电网', '生活缴费', '充值服务', '话费', '电费', '水费', '燃气', '供电', '移动', '联通', '电信']),
    ('医疗健康', ['医院', '诊所', '药', '医疗', '口腔', '体检', '门诊']),
    ('住房物业', ['贝壳', '租房', '天津小屋', '物业', '房东', '公寓', '房屋']),
    ('运动户外', ['体育', '球馆', '运动', '志跃', '全运', '健身', '球']),
    ('文化休闲', ['龙石战争', '游戏', '电影', 'KTV', '演出', '门票', '景点', '棋牌', '乐逸', '湿地', '凯一博', '金币']),
    ('母婴亲子', ['炫娃', '母婴', '亲子', '纸尿', '奶粉', '童装', '婴']),
    ('酒店旅游', ['客栈', '宾馆', '酒店', '民宿', '旅游', '丹水坑', '度假', '旅行']),
    ('日用百货', ['超市', '百货', '便利店', '水果', '生鲜', '朴朴', '零食', '美宜佳', '壹兴', '智慧零售',
                  '三宝', '名门商店', '零食很忙', '轻巧拿', '丰e', '丰e足食', '土特产', '优鲜购']),
    ('服饰装扮', ['服饰', '服装', '衣', '鞋', '帽', '迷你民族']),
    ('美容美发', ['理发', '美容', '美发', '造型', '纯剪', '仟彗', '美发']),
    ('家居家装', ['家纺', '楠木贝壳', '家居', '装修', '窗帘', '床']),
    ('生活服务', ['水电', '按摩', '物流', '家政', '美美家园', '共享按摩椅', '乐摩吧', 'iRest', '维修', '快递', '驿站', '丰巢']),
    ('餐饮美食', ['点餐', '米粉', '米线', '面', '烧烤', '火锅', '咖啡', '奶茶', '炸串', '生煎', '甜品',
                  '双皮奶', '餐馆', '餐厅', '美食', '湘阁里辣', '达美乐', '肯德基', '美团', '喜茶', '霸王茶姬',
                  '书亦', '喜姐', '塔斯汀', '1点点', 'Cotti', 'luckin', '波比艾斯', '合德记', '潮米果',
                  '粿小二', '无解酒馆', '赵记传承', '花和尚', '宵夜', '三好烤', '牛爷烧', '在烤', '张啦啦',
                  '简越', '阿秀', '唐小毛', '肇兴', '铁板豆腐', '炒粉', '桥头煮粉', '亼小面', '零食', '小面',
                  '煮粉', '咖啡', '茶饮', '饮品', '饮', '炭烧', '鸡翅', '吃货卡', '饿了么', '有鲤']),
]
# 明确是个人往来（转账/红包给个人、个人二维码收款）
WECHAT_PERSONAL = [
    '华', '东刚', '六妹', '亚男', '小南瓜', '刘伟', '李美凤', '李儒美', '童心', '石昌胜',
    '李香玲', '蒋晶', 'suu', '珊珊', '秋实菊英', '三月的雪', '张胜华', '微笑', '家明',
    '不知从何说起', '高', '肖新民', 'bpmf', '李恩林', '花开花落', '余红昌', '微信转账到QQ',
    'Linna', '小琳', '杰瑞鼠', '无本万利', '滚马想', '强骏', '🥥', 'Lz', '李美', '谢', '黄', '邓菲', '小岳',
]
WECHAT_PERSONAL_PAT = re.compile(r'^[\u4e00-\u9fa5]{2,3}$|^[\u4e00-\u9fa5]{2,3}\s*\(')


def _norm_name(name):
    """去掉 emoji/符号后的核心商户名，用于个人往来识别。"""
    return re.sub(r'[\U0001F000-\U0001FAFF☀-➿️‍\U0001FA70-\U0001FAFF]', '', name).strip()


def map_wechat(row):
    typ = row['交易类型']
    name = str(row['交易对方'])
    text = name + ' ' + str(row.get('商品', ''))
    if typ in ('转账', '群收款'):
        return '转账往来'
    if typ == '二维码收款':
        return '转账往来'
    if '楠木' in name:          # 楠木贝壳是家居品牌，先于「贝壳」租房判定
        return '家居家装'
    # 商户关键词优先（避免把「朴朴/美团」等短商户名误判为个人）
    for cat, kws in WECHAT_RULES:
        for kw in kws:
            if kw in text:
                return cat
    if name.startswith('商户_'):
        return '转账往来'
    core = _norm_name(name)
    # 个人往来：原名/去 emoji 后精确匹配，或多字个人名出现在核心名中
    if name in WECHAT_PERSONAL or core in WECHAT_PERSONAL:
        return '转账往来'
    for p in WECHAT_PERSONAL:
        if len(p) >= 2 and p in core:
            return '转账往来'
    if WECHAT_PERSONAL_PAT.match(name):
        return '转账往来'
    return '其他'


# 支付宝「交易分类=其他」时的兜底规则（收钱码收款/小众商户），按 交易对方+商品说明 匹配
ALIPAY_OTHER_SPECIAL = [
    ('餐饮美食', ['吃货卡', '饿了么', '炭烧', '鸡翅', '快餐', '餐饮', '饮品']),
    ('网购/平台', ['淘宝', '天猫', '京东', '拼多多', '唯品会']),
    ('交通出行', ['停车场', '高速', '地铁', '车站', 'ETC', '加油']),
    ('医疗健康', ['医院', '药房', '诊所', '体检']),
    ('日用百货', ['超市', '便利店', '生鲜', '水果', '零食']),
    ('文化休闲', ['影院', 'KTV', '门票', '游戏', '景点']),
    ('充值缴费', ['话费', '电费', '水费', '燃气', '会员']),
    ('生活服务', ['快递', '驿站', '洗护', '家政']),
]


def map_alipay(row):
    """支付宝行分类：优先用支付宝自带交易分类；为「其他」时按商户名/商品说明补判。"""
    cat = str(row['交易分类'])
    if cat in ALIPAY_CAT_MAP and ALIPAY_CAT_MAP[cat] != '其他':
        return ALIPAY_CAT_MAP[cat]
    name, desc = str(row['交易对方']), str(row['商品说明'])
    text = name + ' ' + desc
    rules = WECHAT_RULES + ALIPAY_OTHER_SPECIAL
    for cat2, kws in rules:
        for kw in kws:
            if kw in text:
                return cat2
    # 收钱码收款/脱敏个人码：无法识别商户 → 视为个人往来（非消费）
    if '收钱码' in desc or name.startswith('*'):
        return '转账往来'
    return '其他'


def map_citic_bank(rows):
    """中信银行支出分类：消费直付 / 剔除结算 / 储蓄投资 / 转账往来 / 内部转账 / 收入。"""
    consumed = []     # 独立消费
    removed = []      # 重复结算（财付通/支付宝/信用卡还款）
    savings = []      # 储蓄投资
    transfers = []    # 转账往来（家人/个人）
    internal = []     # 本人账户间
    for r in rows:
        if r['收入'] > 0:
            continue
        amt, d = r['支出'], r['明细']
        if amt <= 0:
            continue
        rec = {'日期': r['日期'], '金额': amt, '明细': d, '来源': '中信银行'}
        if '信用卡还款' in d:
            removed.append({**rec, '备注': '信用卡账单还款=重复（对应支付宝信用购消费）'})
        elif '蚂蚁' in d or '基金' in d or '20884215521324210156' in d:
            savings.append({**rec, '备注': '转入蚂蚁基金=储蓄投资'})
        elif '财付通' in d:
            removed.append({**rec, '备注': '财付通=微信支付结算（对应微信流水消费）'})
        elif d.startswith('支付宝') or '支付宝' in d:
            removed.append({**rec, '备注': '支付宝=支付宝结算（对应支付宝流水消费）'})
        elif '大额存单' in d or '银证' in d or '证券' in d or '基金' in d:
            savings.append({**rec, '备注': '储蓄/投资'})
        elif '京东' in d or '网银在线' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '拼多多' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '广州久伴' in d or '房屋租赁' in d:
            consumed.append({**rec, '类别': '住房物业'})
        elif '支取现金' in d or 'ATM' in d:
            consumed.append({**rec, '类别': '现金'})
        elif '岭南通' in d:
            consumed.append({**rec, '类别': '交通出行'})
        elif '聂东刚' in d:
            transfers.append({**rec, '备注': '转家人往来'})
        elif '6214832030228642' in d:   # 转本人招商账户
            internal.append({**rec, '备注': '本人账户间转账'})
        elif '转账' in d:
            transfers.append({**rec, '备注': '银行转账'})
        else:
            consumed.append({**rec, '类别': '其他'})
    return consumed, removed, savings, transfers, internal


def map_cmb_bank(rows):
    consumed, removed, savings, transfers, internal = [], [], [], [], []
    for r in rows:
        amt = r['金额']
        if amt >= 0:
            continue
        amt = -amt
        d = r['明细']
        rec = {'日期': r['日期'], '金额': amt, '明细': d, '来源': '招商银行'}
        if '大额存单' in d or '银证' in d or '证券' in d or '蚂蚁' in d or '基金' in d:
            savings.append({**rec, '备注': '储蓄/投资'})
        elif '1109613270100010508399419' in d:   # 广州久伴房租账户（与中信一致）
            consumed.append({**rec, '类别': '住房物业'})
        elif '聂东刚' in d or base64.b64decode('NjIyMTgwNTU1MDAwMDU3NTQ0Ng==').decode('utf-8') in d:
            transfers.append({**rec, '备注': '转家人往来'})
        elif '广州久伴' in d or '房屋租赁' in d:
            consumed.append({**rec, '类别': '住房物业'})
        elif '岭南通' in d:
            consumed.append({**rec, '类别': '交通出行'})
        elif '淘宝' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '深圳中融' in d or '小额贷款' in d:
            removed.append({**rec, '备注': '贷款/分期还款'})
        elif '转账汇款' in d or '转账' in d:
            transfers.append({**rec, '备注': '银行转账'})
        elif '充值' in d:
            consumed.append({**rec, '类别': '充值缴费'})
        elif '快捷支付' in d or '银联快捷支付' in d:
            consumed.append({**rec, '类别': '其他'})
        else:
            consumed.append({**rec, '类别': '其他'})
    return consumed, removed, savings, transfers, internal


DETAIL_COLS = ['日期', '来源', '对方', '商品', '金额', '备注']


def export_category_detail(consume, transfers, out_dir):
    """输出按类别拆分的流水明细（供本人复核）：Excel 每类一个 sheet + 一份 Markdown。
    consume 为去重后的消费明细（金额为负表示退款冲减）；transfers 为非消费的转账往来明细。"""
    out_xlsx = os.path.join(out_dir, '支出分类明细.xlsx')
    out_md = os.path.join(out_dir, '支出分类明细.md')
    cat_sum = consume.groupby('类别')['金额'].sum().sort_values(ascending=False)

    md = ['# 支出分类流水明细（供复核）\n',
          '> 全部为去重后计入消费的明细，金额为负表示退款（已冲减对应类别）。\n']

    with pd.ExcelWriter(out_xlsx, engine='openpyxl') as writer:
        ov = cat_sum.reset_index()
        ov.columns = ['类别', '金额']
        ov['笔数'] = consume.groupby('类别')['金额'].count().reindex(ov['类别']).values
        ov.to_excel(writer, sheet_name='总览', index=False)

        for cat in cat_sum.index:
            sub = consume[consume['类别'] == cat].sort_values(['来源', '日期'])
            rows = sub[DETAIL_COLS].copy()
            total = round(sub['金额'].sum(), 2)
            tot_row = pd.DataFrame([{'日期': '', '来源': '', '对方': '合计', '商品': '',
                                     '金额': total, '备注': f'{len(sub)} 笔'}])
            sheet = pd.concat([rows, tot_row], ignore_index=True)
            name = re.sub(r'[\\/*?:\[\]]', '·', str(cat))[:31]
            sheet.to_excel(writer, sheet_name=name, index=False)
            ws = writer.sheets[name]
            ws.freeze_panes = 'A2'
            for col, w in zip('ABCDEF', [12, 9, 26, 30, 11, 22]):
                ws.column_dimensions[col].width = w
            md.append(f'\n## {cat}（{total:,.2f} 元 · {len(sub)} 笔）\n')
            md.append('| 日期 | 来源 | 对方 | 商品 | 金额 | 备注 |')
            md.append('| --- | --- | --- | --- | ---: | --- |')
            for _, r in rows.iterrows():
                md.append(f"| {r['日期']} | {r['来源']} | {str(r['对方'])[:26]} | {str(r['商品'])[:26]} | {r['金额']:,.2f} | {str(r['备注'])[:22]} |")

        if transfers is not None and len(transfers):
            tr = transfers.sort_values(['来源', '日期'])
            tr = tr[DETAIL_COLS]
            total_tr = round(tr['金额'].sum(), 2)
            tr2 = pd.concat([tr, pd.DataFrame([{'日期': '', '来源': '', '对方': '合计', '商品': '',
                                                '金额': total_tr, '备注': f'{len(tr)} 笔'}])],
                            ignore_index=True)
            tr2.to_excel(writer, sheet_name='转账往来(非消费)', index=False)
            ws = writer.sheets['转账往来(非消费)']
            ws.freeze_panes = 'A2'
            for col, w in zip('ABCDEF', [12, 9, 26, 30, 11, 22]):
                ws.column_dimensions[col].width = w
            md.append('\n## 转账往来（非消费，复核个人扫码项）\n')
            md.append('| 日期 | 来源 | 对方 | 商品 | 金额 | 备注 |')
            md.append('| --- | --- | --- | --- | ---: | --- |')
            for _, r in tr.iterrows():
                md.append(f"| {r['日期']} | {r['来源']} | {str(r['对方'])[:26]} | {str(r['商品'])[:26]} | {r['金额']:,.2f} | {str(r['备注'])[:22]} |")

    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f'[完成] 分类明细已写入 {out_xlsx} 和 {out_md}')


# ---------------------------------------------------------------- 主流程
def main():
    wx = parse_wechat()
    ap = parse_alipay()
    citic_rows = parse_citic()
    cmb_rows = parse_cmb()

    # ---- 校验 ----
    wx_exp = wx[wx['收支'] == '支出'].copy()
    ap_exp = ap[ap['收支'] == '支出'].copy()
    # 微信退款（收入中的 -退款 类型）
    wx_refund = wx[(wx['收支'] == '收入') & (wx['交易类型'].str.contains('退款', na=False))].copy()
    # 支付宝退款（不计收支中含「退款」）
    ap_refund = alipay_refunds(ap)
    assert abs(wx_exp['金额'].sum() - 34413.55) < 0.01, f"微信支出校验失败: {wx_exp['金额'].sum()}"
    assert abs(ap_exp['金额'].sum() - 45926.43) < 0.01, f"支付宝支出校验失败: {ap_exp['金额'].sum()}"
    assert abs(ap_exp['金额'].sum() - ap_refund['金额'].sum() - 43593.76) < 0.01, \
        f"支付宝净支出校验失败: {ap_exp['金额'].sum() - ap_refund['金额'].sum()}"
    cit_inc = sum(r['收入'] for r in citic_rows)
    cit_out = sum(r['支出'] for r in citic_rows)
    print(f'[校验] 微信支出(毛) {wx_exp["金额"].sum():.2f} 退款 {wx_refund["金额"].sum():.2f}')
    print(f'[校验] 支付宝支出(毛) {ap_exp["金额"].sum():.2f} 退款 {ap_refund["金额"].sum():.2f} 净 {ap_exp["金额"].sum()-ap_refund["金额"].sum():.2f}')
    print(f'[校验] 中信 收入 {cit_inc:,.2f} 支出 {cit_out:,.2f} / 行数 {len(citic_rows)}')

    # ---- 微信分类 ----
    wx_exp = wx_exp.copy()
    wx_exp['类别'] = wx_exp.apply(map_wechat, axis=1)
    wx_detail = wx_exp[['日期', '交易对方', '商品', '金额', '支付方式', '类别', '交易类型']].rename(
        columns={'交易对方': '对方', '支付方式': '支付方式'})

    # ---- 支付宝分类 ----
    ap_exp = ap_exp.copy()
    ap_exp['类别'] = ap_exp.apply(map_alipay, axis=1)
    ap_detail = ap_exp[['日期', '交易分类', '交易对方', '商品说明', '金额', '付款方式', '类别']].rename(
        columns={'交易对方': '对方', '商品说明': '商品', '付款方式': '支付方式'})

    # ---- 银行 ----
    cit_con, cit_rem, cit_sav, cit_tra, cit_int = map_citic_bank(citic_rows)
    cmb_con, cmb_rem, cmb_sav, cmb_tra, cmb_int = map_cmb_bank(cmb_rows)
    bank_consumed = pd.DataFrame(cit_con + cmb_con)
    bank_removed = pd.DataFrame(cit_rem + cmb_rem)
    bank_savings = pd.DataFrame(cit_sav + cmb_sav)
    bank_transfers = pd.DataFrame(cit_tra + cmb_tra)
    bank_internal = pd.DataFrame(cit_int + cmb_int)

    # ---- 消费总表 ----
    wx_exp = wx_exp.copy()
    wx_exp['类别'] = wx_exp.apply(map_wechat, axis=1)
    wx_refund = wx_refund.copy()
    wx_refund['类别'] = wx_refund.apply(map_wechat, axis=1)

    wx_c = pd.DataFrame({
        '来源': '微信',
        '日期': wx_exp['日期'],
        '对方': wx_exp['交易对方'],
        '商品': wx_exp['商品'],
        '金额': wx_exp['金额'],
        '类别': wx_exp['类别'],
        '备注': wx_exp['交易类型'],
    })
    # 退款行金额取负
    wx_r = pd.DataFrame({
        '来源': '微信',
        '日期': wx_refund['日期'],
        '对方': wx_refund['交易对方'],
        '商品': wx_refund['商品'],
        '金额': -wx_refund['金额'].abs(),
        '类别': wx_refund['类别'],
        '备注': '退款:' + wx_refund['交易类型'],
    })
    wx_c = pd.concat([wx_c, wx_r], ignore_index=True)
    wx_c = wx_c[wx_c['类别'] != '转账往来']

    ap_c = pd.DataFrame({
        '来源': '支付宝',
        '日期': ap_exp['日期'],
        '对方': ap_exp['交易对方'],
        '商品': ap_exp['商品说明'],
        '金额': ap_exp['金额'],
        '类别': ap_exp['类别'],
        '备注': ap_exp['付款方式'] + '/' + ap_exp['交易状态'],
    })
    ap_r = pd.DataFrame({
        '来源': '支付宝',
        '日期': ap_refund['日期'],
        '对方': ap_refund['交易对方'],
        '商品': ap_refund['商品说明'],
        '金额': -ap_refund['金额'].abs(),
        '类别': ap_refund['类别'],
        '备注': '退款:' + ap_refund['商品说明'].str[:20],
    })
    ap_c = pd.concat([ap_c, ap_r], ignore_index=True)
    ap_c = ap_c[ap_c['类别'] != '转账往来']

    if not bank_consumed.empty:
        bank_c = pd.DataFrame({
            '来源': bank_consumed['来源'],
            '日期': bank_consumed['日期'],
            '对方': bank_consumed['明细'],
            '商品': '',
            '金额': bank_consumed['金额'],
            '类别': bank_consumed['类别'],
            '备注': '',
        })
    else:
        bank_c = pd.DataFrame(columns=['来源', '日期', '对方', '商品', '金额', '类别', '备注'])

    consume = pd.concat([wx_c, ap_c, bank_c], ignore_index=True)

    # ---- 校验类别汇总 == 消费总额 ----
    total_consume = consume['金额'].sum()
    cat_sum = consume.groupby('类别')['金额'].sum()
    print(f'[校验] 消费总额 {total_consume:,.2f} = 类别合计 {cat_sum.sum():,.2f}')
    print()
    print('=== 支出按类别（去重后）===')
    for cat, amt in cat_sum.sort_values(ascending=False).items():
        n = (consume['类别'] == cat).sum()
        print(f'{amt:>12,.2f}  {n:3d}笔  {cat}')

    # ---- 月度趋势 ----
    consume['月份'] = pd.to_datetime(consume['日期'], errors='coerce').dt.strftime('%Y-%m')
    monthly = consume.groupby('月份')['金额'].sum().sort_index()

    # ---- 往来/储蓄汇总 ----
    if not bank_transfers.empty:
        bank_transfers = bank_transfers[['来源', '日期', '金额', '明细', '备注']]
    if not bank_savings.empty:
        bank_savings = bank_savings[['来源', '日期', '金额', '明细', '备注']]
    if not bank_internal.empty:
        bank_internal = bank_internal[['来源', '日期', '金额', '明细', '备注']]
    if not bank_removed.empty:
        bank_removed = bank_removed[['来源', '日期', '金额', '明细', '备注']]

    # ---- Excel 输出 ----
    with pd.ExcelWriter(os.path.join(OUT, '支出分析.xlsx'), engine='openpyxl') as writer:
        cat_sum_df = cat_sum.reset_index().rename(columns={'index': '类别', '金额': '金额'})
        cat_sum_df.columns = ['类别', '金额']
        cat_sum_df['笔数'] = consume.groupby('类别')['金额'].count().reindex(cat_sum_df['类别']).values
        cat_sum_df['占比'] = (cat_sum_df['金额'] / total_consume * 100).round(2)
        cat_sum_df.to_excel(writer, sheet_name='类别汇总', index=False)
        monthly.reset_index().rename(columns={'月份': '月份', '金额': '支出'}).to_excel(
            writer, sheet_name='月度趋势', index=False)
        consume[['来源', '日期', '对方', '商品', '金额', '类别', '备注']].sort_values(
            ['来源', '日期']).to_excel(writer, sheet_name='消费明细', index=False)
        bank_removed.to_excel(writer, sheet_name='剔除重复结算', index=False)
        bank_savings.to_excel(writer, sheet_name='储蓄投资', index=False)
        bank_transfers.to_excel(writer, sheet_name='转账往来', index=False)
        bank_internal.to_excel(writer, sheet_name='内部转账', index=False)

    # ---- 分类明细导出（供本人复核） ----
    wx_tz = wx_exp.loc[wx_exp['类别'] == '转账往来', ['日期', '交易对方', '商品', '金额', '交易类型']].copy()
    wx_tz = wx_tz.rename(columns={'交易对方': '对方', '交易类型': '备注'})
    wx_tz['来源'] = '微信'
    ap_tz = ap_exp.loc[ap_exp['类别'] == '转账往来', ['日期', '交易对方', '商品说明', '金额', '付款方式']].copy()
    ap_tz = ap_tz.rename(columns={'交易对方': '对方', '商品说明': '商品', '付款方式': '备注'})
    ap_tz['来源'] = '支付宝'
    if len(bank_transfers):
        bank_tz = bank_transfers.rename(columns={'明细': '对方'}).copy()
        bank_tz['商品'] = ''
        bank_tz = bank_tz[['日期', '来源', '对方', '商品', '金额', '备注']]
    else:
        bank_tz = pd.DataFrame(columns=['日期', '来源', '对方', '商品', '金额', '备注'])
    transfers_detail = pd.concat([
        wx_tz[['日期', '来源', '对方', '商品', '金额', '备注']],
        ap_tz[['日期', '来源', '对方', '商品', '金额', '备注']],
        bank_tz,
    ], ignore_index=True)
    export_category_detail(consume, transfers_detail, OUT)

    # ---- 图表 ----
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib import font_manager
        for fp in [r'C:\Windows\Fonts\msyh.ttc', r'C:\Windows\Fonts\msyh.ttf', r'C:\Windows\Fonts\simhei.ttf']:
            if os.path.exists(fp):
                font_manager.fontManager.addfont(fp)
                plt.rcParams['font.family'] = font_manager.FontProperties(fname=fp).get_name()
                break
        plt.rcParams['axes.unicode_minus'] = False

        fig, ax = plt.subplots(figsize=(8, 7))
        cats = cat_sum_df.sort_values('金额', ascending=True)
        colors = plt.cm.tab20.colors
        ax.barh(cats['类别'], cats['金额'], color=[colors[i % 20] for i in range(len(cats))])
        ax.set_title('2025 年消费支出按类别（去重后）')
        ax.set_xlabel('金额（元）')
        for i, v in enumerate(cats['金额']):
            ax.text(v, i, f'{v:,.0f}', va='center', fontsize=8)
        plt.tight_layout()
        plt.savefig(os.path.join(CHART_DIR, 'category_bar.png'), dpi=150)
        plt.close()

        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.plot(monthly.index, monthly.values, marker='o')
        ax.set_title('2025 年每月消费支出（去重后）')
        ax.set_ylabel('金额（元）')
        ax.grid(True, alpha=0.3)
        for x, y in zip(monthly.index, monthly.values):
            ax.text(x, y, f'{y:,.0f}', ha='center', va='bottom', fontsize=8)
        plt.tight_layout()
        plt.savefig(os.path.join(CHART_DIR, 'monthly_trend.png'), dpi=150)
        plt.close()
    except Exception as e:
        print('[图表] 生成失败:', e)

    # ---- Markdown 报告 ----
    md = []
    md.append('# 2025 年度消费支出分析报告\n')
    md.append('> 数据源：微信支付流水、支付宝交易明细、中信银行流水、招商银行流水（均覆盖 2025-01-01 ~ 2025-12-31）\n')
    md.append(f"**去重后消费支出总额：{total_consume:,.2f} 元**\n")
    md.append('## 一、按类别汇总\n')
    md.append('| 类别 | 笔数 | 金额(元) | 占比 |')
    md.append('| --- | ---: | ---: | ---: |')
    for _, r in cat_sum_df.sort_values('金额', ascending=False).iterrows():
        md.append(f"| {r['类别']} | {int(r['笔数'])} | {r['金额']:,.2f} | {r['占比']:.2f}% |")
    md.append('')
    md.append('## 二、月度趋势\n')
    md.append('| 月份 | 支出(元) |')
    md.append('| --- | ---: |')
    for m, v in monthly.items():
        md.append(f'| {m} | {v:,.2f} |')
    md.append('')
    md.append('## 三、去重说明\n')
    md.append('同一笔消费会在「发生点」（微信/支付宝流水）和「结算点」（银行流水）各出现一次，本报告只在发生点计入：\n')
    md.append(f"- 剔除银行**信用卡账单还款**：{bank_removed[bank_removed['明细'].str.contains('信用卡', na=False)]['金额'].sum():,.2f} 元（对应支付宝「江苏银行信用购」等信用消费，已在支付宝流水中计入）")
    removed_cft = bank_removed[bank_removed['明细'].str.contains('财付通', na=False)]['金额'].sum()
    removed_zfb = bank_removed[bank_removed['明细'].str.contains('支付宝', na=False)]['金额'].sum()
    md.append(f"- 剔除银行**财付通(微信)结算**：{removed_cft:,.2f} 元（对应微信流水中的消费）")
    md.append(f"- 剔除银行**支付宝结算**：{removed_zfb:,.2f} 元（对应支付宝流水中的消费）")
    md.append('')
    wx_personal_amt = wx_exp.loc[wx_exp['类别'] == '转账往来', '金额'].sum()
    ap_personal_amt = ap_exp.loc[ap_exp['类别'] == '转账往来', '金额'].sum()
    bank_trf_amt = bank_transfers['金额'].sum()
    md.append('## 四、不计入消费的资金流动\n')
    md.append(f"- **储蓄投资**（大额存单、银证转账、基金转入等）：{bank_savings['金额'].sum():,.2f} 元")
    md.append(f"- **转账往来**：{bank_trf_amt + wx_personal_amt + ap_personal_amt:,.2f} 元"
              f"（银行转账 {bank_trf_amt:,.2f}、微信转个人 {wx_personal_amt:,.2f}、支付宝信用借还等 {ap_personal_amt:,.2f}）")
    md.append(f"- **内部转账**（本人账户间划转）：{bank_internal['金额'].sum():,.2f} 元")
    md.append('')
    md.append('## 五、复核要点\n')
    md.append('- 住房物业含**招商银行 2025-05-12 快捷支付「广州久伴房屋租赁」10,000 元**（按月租 2,484 推算应属房租/押金类，若为可退押金请调整）；另含物业费 1,770.69 元')
    md.append('- 每月房租 2,484 元全年 12 笔（支付宝 6、微信 2、中信 2、招商 2），招商 5/17 为 2,482 元（差额为转账手续费），合计 29,806 元')
    md.append('- 「其他」113.50 元 = 招商银行两笔小额直购 11.7/100 元（无法判定商户）+ 微信「广州天慈」1.8 元')
    md.append('- 若微信/支付宝中向个人的「扫码付款」应视为消费，请告知，可将相应金额从转账往来移回对应类别')
    md.append('')
    md.append('## 六、图表\n')
    md.append('![类别占比](charts/category_bar.png)\n')
    md.append('![月度趋势](charts/monthly_trend.png)\n')
    with open(os.path.join(OUT, '支出分析.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print()
    print(f'[完成] 交付物已写入 {OUT}')


if __name__ == '__main__':
    main()
