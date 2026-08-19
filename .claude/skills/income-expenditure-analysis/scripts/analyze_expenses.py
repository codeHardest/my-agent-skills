# -*- coding: utf-8 -*-
"""
收支流水支出分析：去重 + 按类别统计（参考实现）。

用法:
  py -3.13 analyze_expenses.py --input-dir <流水目录> [--output <输出目录>] [--year 2025] [--title "2025 年度"]

输入目录自动识别（按文件名）:
  微信*.xlsx      → 微信发生点（表头 0 基索引 17）
  支付宝*.csv     → 支付宝发生点（GBK，表头 0 基索引 23）
  中信*.pdf       → 中信银行 PDF（word 级解析）
  招商*.pdf       → 招商银行 PDF（word 级解析）
  其余 *.csv      → 通用银行流水（列: 日期,摘要,金额[带符号],备注）

核心原则: 消费只在发生点计一次；银行「财付通/支付宝/信用卡还款」为重复结算，
剔除单列；银行直付计入；储蓄投资/转账往来/内部转账单列不计入消费。
三条账本口径（按用户要求）：
1. 退款不体现在账单里——退款按 (来源,单号) 冲减原交易行，全部退款整行移除，部分退款按净额单行；
2. 主力购物平台单列 sheet——拼多多/淘宝/京东/抖音 单独拆解（PLATFORM_KEYWORDS 可扩展）；
3. 加班打车报销——网约车支出由单位报销的部分不计入消费，从交通出行剔除并单列，报销在银行收入中识别（金额对账，不确定进复核要点）。

依赖: pandas, openpyxl, pdfplumber, matplotlib（图表）
"""
import os, re, csv, glob, argparse, base64
import pandas as pd
import pdfplumber

# ---------------------------------------------------------------- 统一类别集
CONSUME_CATS = ['餐饮美食', '日用百货', '交通出行', '文化休闲', '充值缴费', '医疗健康',
                '家居家装', '生活服务', '商业服务', '服饰装扮', '住房物业', '美容美发',
                '母婴亲子', '运动户外', '教育培训', '酒店旅游', '爱车养车', '网购/平台', '现金', '其他']
ALIPAY_CAT_MAP = {
    '日用百货': '日用百货', '餐饮美食': '餐饮美食', '交通出行': '交通出行', '文化休闲': '文化休闲',
    '充值缴费': '充值缴费', '医疗健康': '医疗健康', '家居家装': '家居家装', '其他': '其他',
    '生活服务': '生活服务', '商业服务': '商业服务', '服饰装扮': '服饰装扮', '住房物业': '住房物业',
    '美容美发': '美容美发', '母婴亲子': '母婴亲子', '运动户外': '运动户外', '教育培训': '教育培训',
    '酒店旅游': '酒店旅游', '爱车养车': '爱车养车', '信用借还': '转账往来',
}

# ---------------------------------------------------------------- 关键词规则
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
    ('美容美发', ['理发', '美容', '美发', '造型', '纯剪', '仟彗']),
    ('家居家装', ['家纺', '楠木贝壳', '家居', '装修', '窗帘', '床']),
    ('生活服务', ['水电', '按摩', '物流', '家政', '美美家园', '共享按摩椅', '乐摩吧', 'iRest', '维修', '快递', '驿站', '丰巢', '充电宝']),
    ('餐饮美食', ['点餐', '米粉', '米线', '面', '烧烤', '火锅', '咖啡', '奶茶', '炸串', '生煎', '甜品',
                  '双皮奶', '餐馆', '餐厅', '美食', '湘阁里辣', '达美乐', '肯德基', '美团', '喜茶', '霸王茶姬',
                  '书亦', '喜姐', '塔斯汀', '1点点', 'Cotti', 'luckin', '波比艾斯', '合德记', '潮米果',
                  '粿小二', '无解酒馆', '赵记传承', '花和尚', '宵夜', '三好烤', '牛爷烧', '在烤', '张啦啦',
                  '简越', '阿秀', '唐小毛', '肇兴', '铁板豆腐', '炒粉', '桥头煮粉', '亼小面', '零食', '小面',
                  '煮粉', '茶饮', '饮品', '饮', '炭烧', '鸡翅', '吃货卡', '饿了么', '有鲤']),
]
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
# 商户级强覆盖（最高优先级，先于支付宝自带分类/微信关键词）：支付宝自带交易分类可能标错
# （如地铁站「优鲜购」被标为家居家装、小吃摊被标为商业服务/酒店旅游），微信「广州地铁优鲜购」
# 也会被交通出行「地铁」先命中。按 交易对方+商品说明 关键词覆盖。
CATEGORY_OVERRIDES = [
    ('餐饮美食', ['优鲜购', '表哥烤鱼', '阿正特色凉拌菜', '鸡蛋汉堡', '小吃店', '扫码点单']),
    # 广州地铁优鲜购：地铁站鲜食便利店；表哥烤鱼/凉拌菜/鸡蛋汉堡/小吃店：收钱码/经营码小吃摊，
    # 支付宝将其标为 酒店旅游/商业服务，用户定档餐饮美食；「扫码点单店主」是餐饮扫码点单收款码
    ('母婴亲子', ['皇婴汇']),          # 母婴用品店，支付宝将其标为 商业服务
    ('生活服务', ['聚充充', '竹芒']),   # 充电宝租借平台（广东聚充充/深圳竹芒=街电），支付宝走「信用借还」误标
    ('其他', ['**金']),               # 脱敏个人收钱码、无有效分类信息（支付宝误标教育培训）
    ('教育培训', ['课时']),            # 付费课时/课程（志跃体育 4122.00 收款码留言「50课时」），压过运动户外「志跃」
]
# 微信「扫二维码付款」无法分类的小额支出 → 其他（用户规则：≤100 元计入消费，而非转账往来）
QR_OTHER_LIMIT = 100.0
# 交易级覆盖（最高优先）：支付宝导出里商家信息被脱敏（如美团订单只见 it_***@meituan.com），
# 无法用关键词区分同一商户的不同业务，需按 (来源, 日期, 金额) 精确指定。
# 真实账本：美团订单=外卖餐饮；其余美团行（美容美发/文化休闲）不受影响。
TRANSACTION_OVERRIDES = [
    ('餐饮美食', '支付宝', '2025-11-12', '美团', 34.00),
    ('餐饮美食', '支付宝', '2025-11-17', '美团', 26.30),
    ('餐饮美食', '支付宝', '2025-11-18', '美团', 14.20),
    ('餐饮美食', '支付宝', '2025-11-18', '美团', 20.50),
]


def _tx_override(source, date, name, amt):
    """交易级覆盖：命中 (来源, 日期, 金额) 且对方名吻合 → 返回类别。"""
    try:
        amt = float(amt)
    except (TypeError, ValueError):
        return None
    for cat, src, d, n, a in TRANSACTION_OVERRIDES:
        if src == source and d == date and abs(amt - a) < 0.005 and n in str(name):
            return cat
    return None


# 转账/群收款默认视为往来，但对方命中明确的住房/房租关键词时按消费归类
# （如「贝壳廖敏玲」= 贝壳租房平台付房东房租）。只放可靠关键词，避免个人转账误判。
TRANSFER_CATEGORIZE = [
    ('住房物业', ['贝壳', '租房', '物业', '房东', '公寓', '房屋', '房租']),
]
WECHAT_PERSONAL = [
    '华', '东刚', '六妹', '亚男', '小南瓜', '刘伟', '李美凤', '李儒美', '童心', '石昌胜',
    '李香玲', '蒋晶', 'suu', '珊珊', '秋实菊英', '三月的雪', '张胜华', '微笑', '家明',
    '不知从何说起', '高', '肖新民', 'bpmf', '李恩林', '花开花落', '余红昌', '微信转账到QQ',
    'Linna', '小琳', '杰瑞鼠', '无本万利', '滚马想', '强骏', 'Lz', '李美', '谢', '黄', '邓菲', '小岳',
]
WECHAT_PERSONAL_PAT = re.compile(r'^[\u4e00-\u9fa5]{2,3}$|^[\u4e00-\u9fa5]{2,3}\s*\(')

# 银行个人/内部账户识别（按真实流水配置；通用银行 csv 主要靠关键词）
# 家人账号以 base64 保存，避免源码被关键字直接检索到；运行时解码。
BANK_TRANSFER_NAMES = ['聂东刚']
BANK_TRANSFER_ACCOUNTS = [base64.b64decode('NjIyMTgwNTU1MDAwMDU3NTQ0Ng==').decode('utf-8')]
BANK_INTERNAL_ACCOUNTS = ['6214832030228642', '6217680910778096']

# 主力购物平台（按「交易对方/银行明细」关键词识别，供单独拆解 sheet）
PLATFORM_KEYWORDS = [
    ('拼多多', ['拼多多', '拼好货']),
    ('淘宝', ['淘宝', '天猫', '淘特']),
    ('京东', ['京东', '网银在线']),   # 网银在线是京东支付网关
    ('抖音', ['抖音']),
]


def platform_of(text):
    t = str(text)
    for p, kws in PLATFORM_KEYWORDS:
        for kw in kws:
            if kw in t:
                return p
    return '其他平台'


# 加班打车报销识别：网约车支出 冲减 银行报销收入
RIDE_HL_KW = ['滴滴', '网约车', '曹操', 'T3', '享道']       # 打车/网约车支出关键词
# 命中打车关键词但实为零售商户的排除词：如「东网约车便利店」是便利店，不是网约车
# （真实账本 2025-07-09 8.00 曾因此被误判为加班打车）。含这些词的不算打车。
RIDE_NEG_KW = ['便利店', '超市', '商店', '零售', '百货']
REIMBURSE_HINT = ('打车', '滴滴', '网约车', '加班', '差旅', '交通')  # 报销收入须与出行相关
# 已知报销入账方：账号或名称命中即视为报销入账（真实账本：雇主「广州腾讯凯博信息」以「转账…」入账
# 加班打车报销，行文不含「报销」二字，只能靠对方识别）。代发工资行不算（那是工资，非报销）；
# 超过 REIMBURSE_SALARY_FLOOR 的大额入账视为工资/奖金（报销多为小额），不算报销但会在复核要点提示。
REIMBURSE_PAYEES = [('8110901013501308779', '广州腾讯凯博信息')]
REIMBURSE_EXCLUDE = ['代发工资']
REIMBURSE_SALARY_FLOOR = 20000.0


def money(s):
    try:
        return float(str(s).replace(',', ''))
    except Exception:
        return 0.0


def clean(v):
    """Markdown 渲染用：把 NaN/None 变成空串，避免显示 'nan'。"""
    return '' if v is None or pd.isna(v) else str(v)


def _norm_name(name):
    return re.sub(r'[\U0001F000-\U0001FAFF☀-➿️‍\U0001FA70-\U0001FAFF]', '', name).strip()


# ---------------------------------------------------------------- 解析：发生点
def parse_wechat(path):
    df = pd.read_excel(path, header=17)
    df.columns = ['交易时间', '交易类型', '交易对方', '商品', '收支', '金额',
                  '支付方式', '当前状态', '交易单号', '商户单号', '备注']
    df = df[df['交易时间'].notna()].copy()
    df['金额'] = pd.to_numeric(df['金额'], errors='coerce')
    df['日期'] = pd.to_datetime(df['交易时间'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['来源'] = '微信'
    return df


def parse_alipay(path):
    with open(path, encoding='gbk') as f:
        rows = list(csv.reader(f))
    data = [r[:12] for r in rows[24:] if r and r[0].strip() and r[5].strip()]
    df = pd.DataFrame(data, columns=['交易时间', '交易分类', '交易对方', '对方账号', '商品说明',
                                     '收支', '金额', '付款方式', '交易状态', '订单号', '商家单号', '备注'])
    df['金额'] = pd.to_numeric(df['金额'], errors='coerce')
    df['日期'] = pd.to_datetime(df['交易时间'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['来源'] = '支付宝'
    return df


def alipay_refunds(df):
    nb = df[df['收支'] == '不计收支']
    refund = nb[nb['商品说明'].str.contains('退款', na=False)].copy()
    if refund.empty:
        return refund
    exp = df[df['收支'] == '支出'].copy()
    exp['mid'] = exp['商家单号'].str.strip()
    exp['cat'] = exp.apply(map_alipay, axis=1)
    mid_to_cat = {mid: cat for mid, cat in zip(exp['mid'], exp['cat']) if mid}
    refund['mid'] = refund['商家单号'].str.strip()
    refund['类别'] = refund['mid'].map(mid_to_cat).fillna(
        refund.apply(map_alipay, axis=1))
    refund['金额'] = refund['金额'].abs()
    return refund


# ---------------------------------------------------------------- 解析：银行 PDF
AMT_RE = re.compile(r'^[\d,]+\.\d{2}$')


def _word_groups(pdf_path):
    groups = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            lines = {}
            for w in page.extract_words():
                lines.setdefault(round(w['top'] / 4), []).append(w)
            cur = []
            for key in sorted(lines):
                ws = sorted(lines[key], key=lambda w: w['x0'])
                is_date = bool(ws and ws[0]['x0'] < 120 and
                               (re.match(r'^\d{8}$', ws[0]['text']) or
                                re.match(r'^\d{4}-\d{2}-\d{2}$', ws[0]['text'])))
                if is_date:
                    if cur:
                        groups.append(cur)
                    cur = ws
                else:
                    cur = cur + ws if cur else ws
            if cur:
                groups.append(cur)
    return groups


def parse_citic(path):
    """中信银行 PDF。附言是右列、可跨两行竖排的单元格（如「转账…广州腾讯凯博信息科技有限公/司」）。
    按「日期行分带」合并：以每笔交易的日期行为锚，相邻日期中点切分竖带，带内右列字归该笔，
    避免相邻行附言/页脚串入（否则会出现「信用卡还款…广州腾讯凯博」这类污染明细）。"""
    rows = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()
            dates = sorted([w for w in words
                            if w['x0'] < 100 and re.match(r'^\d{8}$', w['text'])],
                           key=lambda w: w['top'])
            for i, d in enumerate(dates):
                lo = (dates[i - 1]['top'] + d['top']) / 2 if i > 0 else d['top'] - 20
                hi = (d['top'] + dates[i + 1]['top']) / 2 if i + 1 < len(dates) else d['top'] + 20
                band = [w for w in words if lo <= w['top'] < hi]

                def col(x):
                    if x < 90:   return 0
                    if x < 157:  return 1
                    if x < 222:  return 2
                    if x < 300:  return 3
                    return 4
                cells = {}
                for w in band:
                    cells.setdefault(col(w['x0']), []).append(w)

                def pick(c):
                    return ''.join(x['text'] for x in cells.get(c, []) if AMT_RE.match(x['text']))
                detail = ''.join(w['text'] for w in band
                                 if w['x0'] >= 265 and not AMT_RE.match(w['text']))
                rows.append({'日期': f"{d['text'][:4]}-{d['text'][4:6]}-{d['text'][6:]}",
                             '收入': money(pick(1)), '支出': money(pick(2)),
                             '余额': money(pick(3)), '明细': detail})
    return rows


def parse_cmb(path):
    """招商银行 PDF。对手/附言是右列、可跨两行竖排的单元格，部分行对手信息直接内联在交易行。
    按「日期行分带」合并：以每笔交易的日期行 top 为锚，相邻日期中点切分出一条竖直带，
    带内所有字（同行交易字 + 右列附言字）归该笔——避免跨行附言串到相邻交易。"""
    rows = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()
            dates = sorted([w for w in words
                            if w['x0'] < 120 and re.match(r'^\d{4}-\d{2}-\d{2}$', w['text'])],
                           key=lambda w: w['top'])
            for i, d in enumerate(dates):
                lo = (dates[i - 1]['top'] + d['top']) / 2 if i > 0 else d['top'] - 20
                hi = (d['top'] + dates[i + 1]['top']) / 2 if i + 1 < len(dates) else d['top'] + 20
                band = [w for w in words if lo <= w['top'] < hi]
                amt = next((money(w['text']) for w in sorted(band, key=lambda w: w['x0'])
                            if re.match(r'^-?[\d,]+\.\d{2}$', w['text'])), None)
                if amt is None:
                    continue
                skip = {'CNY', 'RMB', d['text']}
                parts = [w['text'] for w in sorted(
                            band, key=lambda w: (abs(w['top'] - d['top']), w['top'], w['x0']))
                         if w['text'] not in skip
                         and not re.match(r'^-?[\d,]+\.\d{2}$', w['text'])
                         and not re.fullmatch(r'[A-Za-z]+', w['text'])]
                rows.append({'日期': d['text'], '金额': amt, '明细': ''.join(parts)})
    return rows


def parse_bank_csv(path):
    """通用银行流水 csv：日期,摘要,金额(带符号,负=支出),备注 → (支出行, 收入行)。
    收入行单独返回，供「加班打车报销」等识别，绝不混入支出分流。"""
    expense_rows, income_rows = [], []
    with open(path, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            amt = money(r.get('金额', ''))
            rec = {'日期': r.get('日期', '').strip(),
                   '明细': (r.get('摘要') or '').strip(),
                   '备注': (r.get('备注') or '').strip()}
            if amt < 0:
                expense_rows.append({**rec, '金额': -amt})
            elif amt > 0:
                income_rows.append({**rec, '金额': amt})
    return expense_rows, income_rows


# ---------------------------------------------------------------- 分类
def transfer_or_other(amt):
    """转账往来的最终判定：金额非整百 → 其他（用户规则：真转账多为整百金额，
    非整百的多是消费误标，如 李美凤 109、无本万利 265、杰瑞鼠 20、*巧 169）。"""
    try:
        return '转账往来' if float(amt) % 100 == 0 else '其他'
    except (TypeError, ValueError):
        return '转账往来'


def map_wechat(row):
    typ = row['交易类型']
    name = str(row['交易对方'])
    text = name + ' ' + str(row.get('商品', ''))
    tx = _tx_override('微信', row.get('日期', ''), name, row.get('金额', 0))
    if tx:
        return tx
    if '楠木' in name:
        return '家居家装'
    if typ in ('转账', '群收款'):
        for cat, kws in TRANSFER_CATEGORIZE:     # 转账命中住房/房租关键词 → 按消费归类
            if any(kw in text for kw in kws):
                return cat
        if typ == '群收款' and money(row.get('金额', 0)) <= QR_OTHER_LIMIT:
            return '其他'      # 群收款 = 拼单/团体收款，小额且无法分类 → 其他（消费），如 刘伟 68.45
        return transfer_or_other(row.get('金额', 0))   # 转账：非整百金额 → 其他
    for cat, kws in CATEGORY_OVERRIDES:
        if any(kw in text for kw in kws):
            return cat
    for cat, kws in WECHAT_RULES:
        for kw in kws:
            if kw in text:
                return cat
    # 小额无法分类支付 → 其他（用户规则：≤100 元计入消费）：扫二维码付款/二维码收款（个人码），
    # 以及 商户消费 里未能命中任何关键词的小额支出（如 余红昌 4.00、小岳 10.00 商户消费）。
    # 真实转账（交易类型=转账/群收款）已在上方分流；商户_ 前缀有专门处理（小额→其他）；
    # 仍须排除可识别往来：微信转账到QQ、商品含「转账」字样（如「向QQ账号…转账」）→ 仍按转账往来。
    amt = money(row.get('金额', 0))
    is_qr = typ in ('扫二维码付款', '二维码收款')
    is_small_merchant = typ == '商户消费' and not (name.startswith('商户_') or 'QQ' in text or '转账' in text)
    if amt <= QR_OTHER_LIMIT and (is_qr or is_small_merchant):
        return '其他'
    if name.startswith('商户_'):
        return '其他' if money(row.get('金额', 0)) <= QR_OTHER_LIMIT else transfer_or_other(row.get('金额', 0))   # 小额商户码 → 其他（消费）
    core = _norm_name(name)
    if name in WECHAT_PERSONAL or core in WECHAT_PERSONAL:
        return transfer_or_other(row.get('金额', 0))
    for p in WECHAT_PERSONAL:
        if len(p) >= 2 and p in core:
            return transfer_or_other(row.get('金额', 0))
    if WECHAT_PERSONAL_PAT.match(name):
        return transfer_or_other(row.get('金额', 0))
    return '其他'


def map_alipay(row):
    name, desc = str(row['交易对方']), str(row['商品说明'])
    text = name + ' ' + desc
    tx = _tx_override('支付宝', row.get('日期', ''), name, row.get('金额', 0))
    if tx:
        return tx
    for cat2, kws in CATEGORY_OVERRIDES:       # 商户级覆盖最高优先：支付宝自带分类可能标错
        if any(kw in text for kw in kws):
            return cat2
    cat = str(row['交易分类'])
    if cat in ALIPAY_CAT_MAP and ALIPAY_CAT_MAP[cat] != '其他':
        return ALIPAY_CAT_MAP[cat]
    for cat2, kws in WECHAT_RULES + ALIPAY_OTHER_SPECIAL:
        for kw in kws:
            if kw in text:
                return cat2
    if '收钱码' in desc or name.startswith('*'):
        return transfer_or_other(row.get('金额', 0))   # 收钱码/脱敏个人码：非整百金额 → 其他
    return '其他'


def _bank_split(rows, source):
    """把银行支出行分流：剔除 / 储蓄 / 消费直付 / 转账往来 / 内部转账。"""
    consumed, removed, savings, transfers, internal = [], [], [], [], []
    for r in rows:
        amt, d = r['金额'], r['明细']
        if amt <= 0:
            continue
        rec = {'日期': r['日期'], '金额': amt, '明细': d, '来源': source}
        if '信用卡还款' in d:
            removed.append({**rec, '备注': '信用卡账单还款=重复（对应信用购消费）'})
        elif ('蚂蚁' in d or '基金' in d or '20884215521324210156' in d
              or '大额存单' in d or '银证' in d or '证券' in d):
            savings.append({**rec, '备注': '储蓄/投资（蚂蚁基金/大额存单/银证）'})
        elif '财付通' in d:
            removed.append({**rec, '备注': '财付通=微信支付结算（对应微信流水消费）'})
        elif d.startswith('支付宝') or '支付宝' in d:
            removed.append({**rec, '备注': '支付宝=支付宝结算（对应支付宝流水消费）'})
        elif '京东' in d or '网银在线' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '拼多多' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '淘宝' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '抖音' in d:
            consumed.append({**rec, '类别': '网购/平台'})
        elif '广州久伴' in d or '房屋租赁' in d:
            consumed.append({**rec, '类别': '住房物业'})
        elif '支取现金' in d or 'ATM' in d or '取现' in d:
            consumed.append({**rec, '类别': '现金'})
        elif '岭南通' in d:
            consumed.append({**rec, '类别': '交通出行'})
        elif '充值' in d:
            consumed.append({**rec, '类别': '充值缴费'})
        elif any(n in d for n in BANK_TRANSFER_NAMES) or any(a in d for a in BANK_TRANSFER_ACCOUNTS):
            transfers.append({**rec, '备注': '转家人往来'})
        elif any(a in d for a in BANK_INTERNAL_ACCOUNTS) or '内部转账' in d:
            internal.append({**rec, '备注': '本人账户间转账'})
        elif '转账' in d:
            transfers.append({**rec, '备注': '银行转账'})
        else:
            consumed.append({**rec, '类别': '其他'})
    return consumed, removed, savings, transfers, internal


FAMILY_ENC_FILENAME = 'transfers_family.enc'
FAMILY_HIDE_ACCOUNTS = [base64.b64decode('NjIxNzAwMjk2MDExMjU0NzkzNw==').decode('utf-8'),
                        base64.b64decode('NjIyMTgwNTU1MDAwMDU3NTQ0Ng==').decode('utf-8')]
FAMILY_HIDE_MIN_AMOUNT = 1000.0   # 严格大于该金额才隐藏；≤1,000 的正常展示


def family_enc_path():
    """加密文件存到 SKILL.md 同级目录（skill 根目录），不写进源流水目录/output。"""
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        FAMILY_ENC_FILENAME)


def _fernet_key(password, salt):
    """由密码 + 随机盐派生 Fernet key（PBKDF2-SHA256），密码本身不落盘。"""
    import base64
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600_000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8')))


def split_family_transfers(bank_transfers):
    """把银行转账往来拆成「隐藏加密」与「正常展示」。
    隐藏 = 明细命中 FAMILY_HIDE_ACCOUNTS 账号 且 金额 > FAMILY_HIDE_MIN_AMOUNT。"""
    if bank_transfers is None or len(bank_transfers) == 0:
        return pd.DataFrame(), pd.DataFrame()

    def hid(r):
        d = str(r.get('明细', '') or '')
        return any(a in d for a in FAMILY_HIDE_ACCOUNTS) and money(r.get('金额', 0)) > FAMILY_HIDE_MIN_AMOUNT

    mask = bank_transfers.apply(hid, axis=1)
    return bank_transfers[mask].copy(), bank_transfers[~mask].copy()


def encrypt_family_rows(rows, password):
    """把转家人往来行加密写入 transfers_family.enc（salt + Fernet token）。"""
    import json
    from cryptography.fernet import Fernet
    salt = os.urandom(16)
    payload = json.dumps([{k: ('' if pd.isna(v) else v) for k, v in r.items()}
                          for r in rows], ensure_ascii=False).encode('utf-8')
    token = Fernet(_fernet_key(password, salt)).encrypt(payload)
    with open(family_enc_path(), 'wb') as f:
        f.write(salt + token)


def decrypt_family_rows(password):
    """解密 transfers_family.enc 返回行列表；密码错误则报错退出。"""
    import json
    from cryptography.fernet import Fernet, InvalidToken
    with open(family_enc_path(), 'rb') as f:
        data = f.read()
    salt, token = data[:16], data[16:]
    try:
        payload = Fernet(_fernet_key(password, salt)).decrypt(token)
    except InvalidToken:
        raise SystemExit('[错误] 密码不正确，无法解锁（需与加密时使用的密码一致）')
    return json.loads(payload.decode('utf-8'))


# ---------------------------------------------------------------- 退款冲减 / 加班打车报销
def net_refunds(consume):
    """退款不体现在账单里：按 (来源, 单号) 把退款冲减到原交易行。
    全部退款的交易整行移除；部分退款的按净额单行显示，备注注明已冲减；
    无单号可配对时按同类别的支出行吸收。返回 (净消费明细, 未吸收退款额)。"""
    refunds = consume[consume['金额'] < 0]
    pos = consume[consume['金额'] >= 0]
    if refunds.empty:
        return pos.drop(columns=['单号']), 0.0
    records = pos.to_dict('records')
    unabsorbed = 0.0
    for _, rf in refunds.iterrows():
        rkey = (rf['来源'], str(rf['单号']).strip())
        need = -float(rf['金额'])                       # 需吸收的退款额（正）
        matched = [r for r in records if (r['来源'], str(r['单号']).strip()) == rkey]
        if not matched:                                 # 无单号：按同类别的支出行吸收
            matched = [r for r in records if r['类别'] == rf['类别']]
        for r in sorted(matched, key=lambda x: str(x['日期'])):
            if need <= 0.001:
                break
            amt = float(r['金额'])
            if amt <= need:
                need -= amt
                records.remove(r)                       # 全部退款 → 整行移除
            else:
                r['金额'] = round(amt - need, 2)
                r['备注'] = (str(r['备注']).rstrip() + f'；退款冲减{need:.2f}').lstrip('；')
                need = 0
        if need > 0.001:
            unabsorbed += need                          # 退款 > 可吸收支出，复核要点提示
    out = pd.DataFrame(records, columns=consume.columns).drop(columns=['单号'])
    return out, round(unabsorbed, 2)


def reimburse_income_total(incomes):
    """报销收入合计 R：银行收入行中
    1) 含「报销」且与出行相关（打车/滴滴/加班/差旅/交通）；或
    2) 命中已知报销入账方（REIMBURSE_PAYEES 的账号/名称），且非代发工资、非工资额度。
    返回 (total, 计入明细, 被工资额度排除的入账方行) 供报告对账。"""
    matched, excluded = [], []
    for r in incomes:
        text = f"{r.get('明细', '')} {r.get('备注', '')}"
        is_payee = any(a in text or n in text for a, n in REIMBURSE_PAYEES)
        if '报销' in text and any(k in text for k in REIMBURSE_HINT):
            matched.append((r, '含「报销」+出行关键词'))
        elif is_payee and not any(e in text for e in REIMBURSE_EXCLUDE):
            if float(r['金额']) < REIMBURSE_SALARY_FLOOR:
                matched.append((r, '命中报销入账方'))
            else:
                excluded.append(r)                          # 工资额度 → 复核要点提示
    return round(sum(float(r['金额']) for r, _ in matched), 2), matched, excluded


def extract_work_rides(consume, reimburse_total):
    """加班打车报销：报销收入冲减网约车支出，从消费中剔除。
    剔除部分单列「加班打车(已报销)」，不计入消费。返回 (净消费, 已报销行, 复核提示)。"""
    if reimburse_total <= 0:
        return consume, pd.DataFrame(), ''
    ride_mask = (consume['对方'].astype(str).str.contains('|'.join(RIDE_HL_KW), na=False)
                 & ~consume['对方'].astype(str).str.contains('|'.join(RIDE_NEG_KW), na=False))
    ride = consume[ride_mask].copy()
    if ride.empty:
        return consume, pd.DataFrame(), ''
    ride_total = ride['金额'].sum()
    work_amt = min(reimburse_total, ride_total)
    need = work_amt
    work_rows, drop_idx = [], []
    for idx, r in ride.sort_values('日期').iterrows():
        if need <= 0.001:
            break
        amt = float(r['金额'])
        if amt <= need:
            need -= amt
            work_rows.append(r.copy())                  # 整笔已报销 → 整行剔除
            drop_idx.append(idx)
        else:
            work_rows.append(r.copy())
            work_rows[-1]['金额'] = round(need, 2)      # 仅剔除已报销部分
            consume.at[idx, '金额'] = round(amt - need, 2)
            consume.at[idx, '备注'] = (str(consume.at[idx, '备注']).rstrip() + '；部分已报销剔除').lstrip('；')
            need = 0
    consume = consume.drop(drop_idx)
    work = pd.DataFrame(work_rows, columns=consume.columns)
    if not work.empty:
        work['备注'] = work['备注'].map(
            lambda s: (str(s).rstrip() + '；加班打车已由单位报销').lstrip('；'))
    note = ''
    if reimburse_total > ride_total:
        note = f'报销收入 {reimburse_total:,.2f} 元 > 网约车支出 {ride_total:,.2f} 元，多出部分请确认'
    elif ride_total > reimburse_total:
        note = f'网约车支出 {ride_total:,.2f} 元中已报销 {work_amt:,.2f} 元，剩余 {ride_total - work_amt:,.2f} 元仍计入交通出行'
    return consume, work, note
DETAIL_COLS = ['日期', '来源', '对方', '商品', '金额', '备注']


def cat_order_other_last(series):
    """类别排序索引：按金额降序，但「其他」固定置底（用户规则，无论金额大小）。"""
    order = series.sort_values(ascending=False).index.tolist()
    return [c for c in order if c != '其他'] + (['其他'] if '其他' in order else [])


def cat_df_order_other_last(df, by='金额', ascending=False):
    """类别 DataFrame 排序：按 by 列排，但「其他」行固定置底（用户规则）。"""
    df = df.sort_values(by, ascending=ascending)
    return pd.concat([df[df['类别'] != '其他'], df[df['类别'] == '其他']], ignore_index=True)


def export_category_detail(consume, transfers, out_dir):
    out_xlsx = os.path.join(out_dir, '支出分类明细.xlsx')
    out_md = os.path.join(out_dir, '支出分类明细.md')
    cat_sum = consume.groupby('类别')['金额'].sum()
    order = cat_order_other_last(cat_sum)
    md = ['# 支出分类流水明细（供复核）\n',
          '> 全部为去重后计入消费的明细。退款已按净额冲减，不再单列退款行；'
          '全部退款的交易整笔移除，部分退款的按净额显示并备注。\n']
    with pd.ExcelWriter(out_xlsx, engine='openpyxl') as writer:
        ov = cat_sum.reindex(order).reset_index()
        ov.columns = ['类别', '金额']
        ov['笔数'] = consume.groupby('类别')['金额'].count().reindex(ov['类别']).values
        ov.to_excel(writer, sheet_name='总览', index=False)
        for cat in order:
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
                md.append(f"| {clean(r['日期'])} | {clean(r['来源'])} | {clean(r['对方'])[:40]} | {clean(r['商品'])[:26]} | {r['金额']:,.2f} | {clean(r['备注'])[:22]} |")
        if transfers is not None and len(transfers):
            tr = transfers.sort_values(['来源', '日期'])[DETAIL_COLS]
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
                md.append(f"| {clean(r['日期'])} | {clean(r['来源'])} | {clean(r['对方'])[:40]} | {clean(r['商品'])[:26]} | {r['金额']:,.2f} | {clean(r['备注'])[:22]} |")
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f'[完成] 分类明细已写入 {out_xlsx} 和 {out_md}')


# ---------------------------------------------------------------- 主流程
def discover_sources(input_dir):
    """按文件名自动识别各来源文件。返回 (微信xlsx, 支付宝csv, [中信pdf], [招商pdf], [银行csv])。"""
    # 跳过 Excel 锁/临时文件（~$ 前缀，如文件正被 Excel 打开时的 `~$微信…xlsx`），避免误当源文件读取
    files = [f for f in os.listdir(input_dir) if not f.startswith('~$')]
    def first(*keys, ext=None):
        for k in keys:
            for f in files:
                if k in f and (ext is None or f.endswith(ext)):
                    return os.path.join(input_dir, f)
        return None
    wx = first('微信', ext='.xlsx')
    ap = first('支付宝', ext='.csv')
    # 中信 PDF 文件名可能是哈希（如 lszm4...），不含「中信」字样——凡「非招商」的 PDF 兜底按中信格式尝试
    cit = [os.path.join(input_dir, f) for f in files if f.endswith('.pdf') and ('中信' in f or '招商' not in f)]
    cmb = [os.path.join(input_dir, f) for f in files if f.endswith('.pdf') and '招商' in f]
    bank_csvs = [os.path.join(input_dir, f) for f in files if f.endswith('.csv') and '支付宝' not in f]
    return wx, ap, cit, cmb, bank_csvs


def main():
    ap = argparse.ArgumentParser(description='收支流水支出分析：去重 + 按类别统计')
    ap.add_argument('--input-dir', default=None, help='流水文件所在目录（自动识别来源）')
    ap.add_argument('--output', default=None, help='输出目录（默认 input_dir/output）')
    ap.add_argument('--year', default='2025', help='报告年份')
    ap.add_argument('--title', default=None, help='报告标题（默认 "{year} 年度消费支出分析报告"）')
    ap.add_argument('--decode', action='store_true',
                    help='安全词：解锁查看被隐藏的转家人往来（密码经环境变量 FAMILY_TRANSFER_KEY 提供，不落盘）')
    args = ap.parse_args()

    # ---- 安全词 decode：解锁查看隐藏的转家人往来（不依赖 input-dir）----
    if args.decode:
        pw = os.environ.get('FAMILY_TRANSFER_KEY', '')
        if not pw:
            raise SystemExit('[错误] --decode 需密码：请先设置环境变量 FAMILY_TRANSFER_KEY 再运行')
        rows = decrypt_family_rows(pw)
        total = sum(float(r['金额']) for r in rows)
        print(f'=== 转家人往来（已从汇总隐藏，共 {len(rows)} 笔，合计 {total:,.2f} 元）===')
        print(f"{'日期':<12}{'金额':>13}  明细")
        for r in sorted(rows, key=lambda x: str(x['日期'])):
            print(f"{str(r['日期']):<12}{float(r['金额']):>13,.2f}  {r['明细']}")
        print('=== 查看完毕，数据仍加密保存（密码不落盘）===')
        return

    if not args.input_dir:
        raise SystemExit('[错误] 需要 --input-dir <流水目录>（除非使用 --decode）')

    HERE = os.path.abspath(args.input_dir)
    OUT = os.path.abspath(args.output) if args.output else os.path.join(HERE, 'output')
    CHART_DIR = os.path.join(OUT, 'charts')
    os.makedirs(CHART_DIR, exist_ok=True)

    wx_path, ap_path, cit_pdfs, cmb_pdfs, bank_csvs = discover_sources(HERE)
    if not wx_path or not ap_path:
        print(f'[错误] 未找到微信/支付宝流水文件（目录 {HERE}）')
        return

    # ---- 解析 ----
    wx = parse_wechat(wx_path)
    apdf = parse_alipay(ap_path)
    bank_rows, bank_incomes = [], []
    for p in cit_pdfs:                                  # 中信：收入/支出双列
        for r in parse_citic(p):
            if r['支出'] > 0:
                bank_rows.append({'日期': r['日期'], '金额': r['支出'], '明细': r['明细'], '备注': ''})
            if r['收入'] > 0:
                bank_incomes.append({'日期': r['日期'], '金额': r['收入'], '明细': r['明细'], '备注': ''})
    for p in cmb_pdfs:                                  # 招商：带符号金额，正=收入
        for r in parse_cmb(p):
            (bank_incomes if r['金额'] > 0 else bank_rows).append(
                {'日期': r['日期'], '金额': abs(r['金额']), '明细': r['明细'], '备注': ''})
    for p in bank_csvs:
        exp_rows, inc_rows = parse_bank_csv(p)
        bank_rows += exp_rows
        bank_incomes += inc_rows

    # ---- 校验（与文件自带汇总比对，这里用已知真实值；新数据改这里）----
    # 微信「当前状态 = 已全额退款」的行无需计入（用户规则）：整笔已退，支出侧与退款侧都不再出现。
    # 不依赖退款单号配对（全额退款的退款行商户单号多为空，现有 (来源,单号) 配对会落空）。
    wx_exp = wx[(wx['收支'] == '支出') & ~wx['当前状态'].astype(str).str.contains('全额退款', na=False)].copy()
    ap_exp = apdf[apdf['收支'] == '支出'].copy()
    wx_refund = wx[(wx['收支'] == '收入') & (wx['交易类型'].str.contains('退款', na=False))
                   & ~wx['当前状态'].astype(str).str.contains('全额退款', na=False)].copy()
    ap_refund = alipay_refunds(apdf)
    print(f'[校验] 微信 支出(毛) {wx_exp["金额"].sum():,.2f} 退款 {wx_refund["金额"].sum():,.2f}')
    print(f'[校验] 支付宝 支出(毛) {ap_exp["金额"].sum():,.2f} 退款 {ap_refund["金额"].sum():,.2f} '
          f'净 {ap_exp["金额"].sum() - ap_refund["金额"].sum():,.2f}')
    if cit_pdfs or cmb_pdfs:
        print(f'[校验] 银行 PDF 行数 {len(bank_rows)}（建议对照 PDF 页脚汇总）')

    # ---- 分类 ----
    wx_exp = wx_exp.copy()
    wx_exp['类别'] = wx_exp.apply(map_wechat, axis=1)
    ap_exp = ap_exp.copy()
    ap_exp['类别'] = ap_exp.apply(map_alipay, axis=1)

    bank_consumed, bank_removed, bank_savings, bank_transfers, bank_internal = _bank_split(bank_rows, '银行')

    # ---- 消费总表（微信/支付宝按发生点 + 退款冲减 + 银行直付）----
    # 带 单号 列：退款按 (来源,单号) 冲减到原交易行，之后 net_refunds 会移除该列。
    wx_refund = wx_refund.copy()
    wx_refund['类别'] = wx_refund.apply(map_wechat, axis=1)
    wx_c = pd.DataFrame({'来源': '微信', '日期': wx_exp['日期'], '对方': wx_exp['交易对方'],
                         '商品': wx_exp['商品'], '金额': wx_exp['金额'], '类别': wx_exp['类别'],
                         '备注': wx_exp['交易类型'], '单号': wx_exp['商户单号'].astype(str).str.strip()})
    wx_r = pd.DataFrame({'来源': '微信', '日期': wx_refund['日期'], '对方': wx_refund['交易对方'],
                         '商品': wx_refund['商品'], '金额': -wx_refund['金额'].abs(),
                         '类别': wx_refund['类别'], '备注': '退款:' + wx_refund['交易类型'],
                         '单号': wx_refund['商户单号'].astype(str).str.strip()})
    wx_c = pd.concat([wx_c, wx_r], ignore_index=True)
    wx_c = wx_c[wx_c['类别'] != '转账往来']

    ap_c = pd.DataFrame({'来源': '支付宝', '日期': ap_exp['日期'], '对方': ap_exp['交易对方'],
                         '商品': ap_exp['商品说明'], '金额': ap_exp['金额'], '类别': ap_exp['类别'],
                         '备注': ap_exp['付款方式'] + '/' + ap_exp['交易状态'],
                         '单号': ap_exp['商家单号'].astype(str).str.strip()})
    ap_r = pd.DataFrame({'来源': '支付宝', '日期': ap_refund['日期'], '对方': ap_refund['交易对方'],
                         '商品': ap_refund['商品说明'], '金额': -ap_refund['金额'].abs(),
                         '类别': ap_refund['类别'], '备注': '退款:' + ap_refund['商品说明'].str[:20],
                         '单号': ap_refund['商家单号'].astype(str).str.strip()})
    ap_c = pd.concat([ap_c, ap_r], ignore_index=True)
    ap_c = ap_c[ap_c['类别'] != '转账往来']

    bank_c = pd.DataFrame({'来源': [c['来源'] for c in bank_consumed],
                           '日期': [c['日期'] for c in bank_consumed],
                           '对方': [c['明细'] for c in bank_consumed],
                           '商品': '', '金额': [c['金额'] for c in bank_consumed],
                           '类别': [c['类别'] for c in bank_consumed], '备注': '', '单号': ''}) \
        if bank_consumed else pd.DataFrame(columns=['来源', '日期', '对方', '商品', '金额', '类别', '备注', '单号'])

    consume = pd.concat([wx_c, ap_c, bank_c], ignore_index=True)

    # ---- 退款冲减（退款不体现在账单里）+ 加班打车报销剔除 ----
    total_refund = round(wx_refund['金额'].abs().sum() + ap_refund['金额'].abs().sum(), 2)
    reimburse_income, reimburse_rows, reimburse_excl = reimburse_income_total(bank_incomes)
    consume, unabsorbed_refund = net_refunds(consume)
    consume, work_rides, ride_note = extract_work_rides(consume, reimburse_income)

    # ---- 校验类别汇总 == 消费总额 ----
    total_consume = consume['金额'].sum()
    cat_sum = consume.groupby('类别')['金额'].sum()
    assert abs(cat_sum.sum() - total_consume) < 0.01, f'类别合计 {cat_sum.sum():,.2f} != 消费总额 {total_consume:,.2f}'
    print(f'[校验] 消费总额 {total_consume:,.2f} == 类别合计 {cat_sum.sum():,.2f}')
    print('=== 支出按类别（去重后）===')
    for cat in cat_order_other_last(cat_sum):
        amt = cat_sum[cat]
        print(f'{amt:>12,.2f}  {(consume["类别"] == cat).sum():3d}笔  {cat}')
    if not work_rides.empty:
        print(f'[提示] 加班打车已报销 {work_rides["金额"].sum():,.2f} 元（不计入消费）')
    if unabsorbed_refund > 0:
        print(f'[提示] 有 {unabsorbed_refund:,.2f} 元退款未能完全冲减，见复核要点')

    consume['月份'] = pd.to_datetime(consume['日期'], errors='coerce').dt.strftime('%Y-%m')
    monthly = consume.groupby('月份')['金额'].sum().sort_index()

    # ---- 主力购物平台拆解（拼多多/淘宝/京东/抖音）----
    platform_detail = consume[consume['金额'] > 0].copy()
    platform_detail['平台'] = platform_detail['对方'].map(platform_of)
    platform_detail = platform_detail[platform_detail['平台'] != '其他平台']

    bank_transfers = pd.DataFrame(bank_transfers)
    bank_savings = pd.DataFrame(bank_savings)
    bank_internal = pd.DataFrame(bank_internal)
    bank_removed = pd.DataFrame(bank_removed)
    for d in (bank_transfers, bank_savings, bank_internal, bank_removed):
        if not d.empty:
            d['明细'] = d['明细']

    # ---- Excel 输出 ----
    cat_sum_df = cat_sum.reset_index()
    cat_sum_df.columns = ['类别', '金额']
    cat_sum_df['笔数'] = consume.groupby('类别')['金额'].count().reindex(cat_sum_df['类别']).values
    cat_sum_df['占比'] = (cat_sum_df['金额'] / total_consume * 100).round(2)
    cat_sum_df = cat_df_order_other_last(cat_sum_df, '金额')   # 「其他」固定置底
    # ---- 转账往来合并（银行 + 微信 + 支付宝），主表与报告口径一致 ----
    wx_tz = wx_exp.loc[wx_exp['类别'] == '转账往来', ['日期', '交易对方', '商品', '金额', '交易类型']].copy()
    wx_tz = wx_tz.rename(columns={'交易对方': '对方', '交易类型': '备注'})
    wx_tz['来源'] = '微信'
    ap_tz = ap_exp.loc[ap_exp['类别'] == '转账往来', ['日期', '交易对方', '商品说明', '金额', '付款方式']].copy()
    ap_tz = ap_tz.rename(columns={'交易对方': '对方', '商品说明': '商品', '付款方式': '备注'})
    ap_tz['来源'] = '支付宝'
    # 转家人往来：不体现在任何汇总里（Excel/明细 md/报告），加密保存到 SKILL.md 同级 transfers_family.enc。
    fam_tz, bank_tz = split_family_transfers(bank_transfers)
    bank_tz = bank_tz.rename(columns={'明细': '对方'}).copy()
    bank_tz['商品'] = ''
    if not bank_tz.empty:
        bank_tz = bank_tz[['日期', '来源', '对方', '商品', '金额', '备注']]
    else:
        bank_tz = pd.DataFrame(columns=['日期', '来源', '对方', '商品', '金额', '备注'])
    if not fam_tz.empty:
        enc_pw = os.environ.get('FAMILY_TRANSFER_KEY', '')
        if enc_pw:
            try:
                encrypt_family_rows(fam_tz.to_dict('records'), enc_pw)
                print(f'[加密] 转家人往来 {len(fam_tz)} 笔 {fam_tz["金额"].sum():,.2f} 元已加密隐藏'
                      f' → {family_enc_path()}')
            except Exception as e:
                print(f'[警告] 转家人往来已隐藏，但加密失败（{e}），请检查 cryptography 是否安装')
        else:
            print(f'[警告] 转家人往来 {len(fam_tz)} 笔 {fam_tz["金额"].sum():,.2f} 元已从汇总隐藏，'
                  f'但未设置 FAMILY_TRANSFER_KEY，未生成加密文件（源流水仍在，可重跑加密）')
    transfers_detail = pd.concat([
        wx_tz[['日期', '来源', '对方', '商品', '金额', '备注']],
        ap_tz[['日期', '来源', '对方', '商品', '金额', '备注']],
        bank_tz], ignore_index=True)
    with pd.ExcelWriter(os.path.join(OUT, '支出分析.xlsx'), engine='openpyxl') as writer:
        cat_sum_df.to_excel(writer, sheet_name='类别汇总', index=False)
        monthly.reset_index().rename(columns={'月份': '月份', '金额': '支出'}).to_excel(
            writer, sheet_name='月度趋势', index=False)
        consume[['来源', '日期', '对方', '商品', '金额', '类别', '备注']].sort_values(
            ['来源', '日期']).to_excel(writer, sheet_name='消费明细', index=False)
        bank_removed.to_excel(writer, sheet_name='剔除重复结算', index=False)
        bank_savings.to_excel(writer, sheet_name='储蓄投资', index=False)
        transfers_detail.to_excel(writer, sheet_name='转账往来', index=False)
        bank_internal.to_excel(writer, sheet_name='内部转账', index=False)
        if not platform_detail.empty:                       # 主力购物平台：汇总 + 明细
            psum = platform_detail.groupby('平台')['金额'].agg(['sum', 'count']).reset_index()
            psum.columns = ['平台', '金额', '笔数']
            psum = psum.sort_values('金额', ascending=False)
            psum.to_excel(writer, sheet_name='主力购物平台', index=False)
            det = platform_detail[['平台', '来源', '日期', '对方', '商品', '金额']].sort_values(
                ['平台', '日期'])
            det.to_excel(writer, sheet_name='主力购物平台', startrow=len(psum) + 2, index=False)
            ws = writer.sheets['主力购物平台']
            ws.freeze_panes = 'A2'
            for col, w in zip('ABCDEF', [12, 9, 12, 26, 30, 11]):
                ws.column_dimensions[col].width = w
        if not work_rides.empty:                            # 加班打车(已报销)，不计入消费
            work_rides[['来源', '日期', '对方', '金额', '备注']].to_excel(
                writer, sheet_name='加班打车(已报销)', index=False)

    # ---- 分类明细导出 ----
    export_category_detail(consume, transfers_detail, OUT)

    # ---- 图表 ----
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib import font_manager
        for fp in [r'C:\Windows\Fonts\msyh.ttc', r'C:\Windows\Fonts\msyh.ttf',
                   r'C:\Windows\Fonts\simhei.ttf', r'/System/Library/Fonts/PingFang.ttc']:
            if os.path.exists(fp):
                font_manager.fontManager.addfont(fp)
                plt.rcParams['font.family'] = font_manager.FontProperties(fname=fp).get_name()
                break
        plt.rcParams['axes.unicode_minus'] = False
        fig, ax = plt.subplots(figsize=(8, 7))
        cats = cat_df_order_other_last(cat_sum_df, '金额', ascending=True)
        colors = plt.cm.tab20.colors
        ax.barh(cats['类别'], cats['金额'], color=[colors[i % 20] for i in range(len(cats))])
        ax.set_title(f'{args.year} 年消费支出按类别（去重后）')
        ax.set_xlabel('金额（元）')
        for i, v in enumerate(cats['金额']):
            ax.text(v, i, f'{v:,.0f}', va='center', fontsize=8)
        plt.tight_layout()
        plt.savefig(os.path.join(CHART_DIR, 'category_bar.png'), dpi=150)
        plt.close()
        fig, ax = plt.subplots(figsize=(9, 4.5))
        ax.plot(monthly.index, monthly.values, marker='o')
        ax.set_title(f'{args.year} 年每月消费支出（去重后）')
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
    sources = []
    if wx_path: sources.append('微信支付流水')
    if ap_path: sources.append('支付宝交易明细')
    for p in cit_pdfs: sources.append('中信银行流水')
    for p in cmb_pdfs: sources.append('招商银行流水')
    for p in bank_csvs: sources.append('银行流水')
    title = args.title or f'{args.year} 年度消费支出分析报告'
    md = [f'# {title}\n']
    _dts = pd.to_datetime(consume['日期'], errors='coerce').dropna()
    _cov = (f'{_dts.min():%Y-%m-%d} ~ {_dts.max():%Y-%m-%d}') if not _dts.empty else f'{args.year} 全年'
    md.append(f'> 数据源：{"、".join(sources)}（覆盖 {_cov}）\n')
    md.append(f'**去重后消费支出总额：{total_consume:,.2f} 元**\n')
    md.append('## 一、按类别汇总\n')
    md.append('| 类别 | 笔数 | 金额(元) | 占比 |')
    md.append('| --- | ---: | ---: | ---: |')
    for _, r in cat_sum_df.iterrows():
        md.append(f"| {r['类别']} | {int(r['笔数'])} | {r['金额']:,.2f} | {r['占比']:.2f}% |")
    md.append('')
    md.append('## 二、月度趋势\n')
    md.append('| 月份 | 支出(元) |')
    md.append('| --- | ---: |')
    for m, v in monthly.items():
        md.append(f'| {m} | {v:,.2f} |')
    md.append('')
    cn_num = ['一', '二', '三', '四', '五', '六', '七', '八', '九']
    has_plat = 1 if not platform_detail.empty else 0
    if has_plat:
        md.append('## 三、主力购物平台\n')
        md.append('拼多多/淘宝/京东/抖音 上的消费小计（按交易对方匹配，**含全品类**，不限「网购/平台」类别）：\n')
        psum = platform_detail.groupby('平台')['金额'].agg(['sum', 'count'])
        md.append('| 平台 | 笔数 | 金额(元) |')
        md.append('| --- | ---: | ---: |')
        for p, row in psum.sort_values('sum', ascending=False).iterrows():
            md.append(f'| {p} | {int(row["count"])} | {row["sum"]:,.2f} |')
        md.append('')
    md.append(f'## {cn_num[2 + has_plat]}、去重说明\n')
    md.append('同一笔消费会在「发生点」（微信/支付宝流水）和「结算点」（银行流水）各出现一次，本报告只在发生点计入：\n')
    rem = bank_removed
    if not rem.empty:
        cr = rem[rem['明细'].str.contains('信用卡', na=False)]['金额'].sum()
        cf = rem[rem['明细'].str.contains('财付通', na=False)]['金额'].sum()
        az = rem[rem['明细'].str.contains('支付宝', na=False)]['金额'].sum()
        md.append(f"- 剔除银行**信用卡账单还款**：{cr:,.2f} 元（对应信用购消费，已在支付宝流水中计入）")
        md.append(f"- 剔除银行**财付通(微信)结算**：{cf:,.2f} 元（对应微信流水中的消费）")
        md.append(f"- 剔除银行**支付宝结算**：{az:,.2f} 元（对应支付宝流水中的消费）")
    md.append('')
    wx_pa = wx_exp.loc[wx_exp['类别'] == '转账往来', '金额'].sum()
    ap_pa = ap_exp.loc[ap_exp['类别'] == '转账往来', '金额'].sum()
    bk_tr = bank_tz['金额'].sum() if not bank_tz.empty else 0.0   # 不含转家人往来（已隐藏加密）
    md.append(f'## {cn_num[3 + has_plat]}、不计入消费的资金流动\n')
    md.append(f"- **储蓄投资**（大额存单、银证转账、基金转入等）：{bank_savings['金额'].sum() if not bank_savings.empty else 0.0:,.2f} 元")
    md.append(f"- **转账往来**：{bk_tr + wx_pa + ap_pa:,.2f} 元"
              f"（银行转账 {bk_tr:,.2f}、微信转个人 {wx_pa:,.2f}、支付宝信用借还等 {ap_pa:,.2f}"
              + ('；指定账号 >1,000 元转家人往来已加密隐藏' if not fam_tz.empty else '') + '）')
    md.append(f"- **内部转账**（本人账户间划转）：{bank_internal['金额'].sum() if not bank_internal.empty else 0.0:,.2f} 元")
    if not work_rides.empty:
        md.append(f"- **加班打车(已报销)**：{work_rides['金额'].sum():,.2f} 元"
                  f"（网约车支出由单位报销，不计入消费；对应银行收入报销 {reimburse_income:,.2f} 元）")
        for r, why in reimburse_rows:
            md.append(f"  - {r['日期']} 入账 {r['金额']:,.2f} 元（{str(r['明细'])[:36]}）— {why}")
    md.append('')
    # 复核要点：动态生成
    md.append(f'## {cn_num[4 + has_plat]}、复核要点\n')
    other_rows = consume[consume['类别'] == '其他']
    if not other_rows.empty:
        parts = '、'.join(f"{r['来源']}「{str(r['对方'])[:18]}」{r['金额']:,.2f}" for _, r in other_rows.iterrows())
        md.append(f"- 「其他」{other_rows['金额'].sum():,.2f} 元 = {parts}（无法判定商户，请核对）")
    big_rent = consume[(consume['类别'] == '住房物业') & (consume['金额'] >= 5000)]
    for _, r in big_rent.iterrows():
        md.append(f"- 住房物业含 **{r['来源']} {r['日期']}「{str(r['对方'])[:24]}」{r['金额']:,.2f} 元**（大额，请确认是否押金/可退）")
    if total_refund > 0:
        md.append(f"- 退款冲减共 {total_refund:,.2f} 元（退款已按净额冲减，明细不单列退款行；全部退款的交易不再出现）")
    if unabsorbed_refund > 0:
        md.append(f"- **{unabsorbed_refund:,.2f} 元退款未能找到对应支出行完全冲减**，请核对订单号")
    if ride_note:
        md.append(f"- {ride_note}")
    if reimburse_excl:
        names = '、'.join(sorted({n for a, n in REIMBURSE_PAYEES}))
        for r in reimburse_excl:
            md.append(f"- 入账方「{names}」{r['日期']} 入账 {r['金额']:,.2f} 元为工资额度"
                      f"（≥{REIMBURSE_SALARY_FLOOR:,.0f} 元），未计入报销，请核对是否为工资/奖金")
    if not platform_detail.empty and '其他平台' in set(platform_detail['平台']):
        md.append('- 主力购物平台表中含「其他平台」项，如需纳入更多平台请补充关键词')
    md.append('- 微信/支付宝向个人的「扫码付款」默认视为转账往来；若应算消费，请告知，相应金额可从转账往来移回对应类别')
    md.append('')
    md.append(f'## {cn_num[5 + has_plat]}、图表\n')
    md.append('![类别占比](charts/category_bar.png)\n')
    md.append('![月度趋势](charts/monthly_trend.png)\n')
    with open(os.path.join(OUT, '支出分析.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f'\n[完成] 交付物已写入 {OUT}')


if __name__ == '__main__':
    main()
