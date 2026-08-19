# -*- coding: utf-8 -*-
"""
生成自包含 HTML 交互账本（消费账本-2025.html）。
复用 skill 的分析脚本（analyze_expenses.py）同一管道，把结果组装成 ledger_data.json
并注入到 ledger_template.html 的 `const DATA = /*__DATA__*/null;` 占位符。

用法: py -3.13 build_ledger.py --input-dir <流水目录> [--template output/ledger_template.html]
"""
import os
import re
import json
import argparse
import importlib.util

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_SCRIPT = os.path.join(os.path.dirname(os.path.dirname(HERE)), '.claude', 'skills',
                            'income-expenditure-analysis', 'scripts', 'analyze_expenses.py')


def load_analyzer():
    spec = importlib.util.spec_from_file_location('analyze_expenses', SKILL_SCRIPT)
    ae = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ae)
    return ae


def run_pipeline(ae, src_dir):
    """复刻 analyze_expenses.main() 的关键数据流，返回组装 JSON 所需的中间结果。"""
    wx_path, ap_path, cit_pdfs, cmb_pdfs, bank_csvs = ae.discover_sources(src_dir)
    if not wx_path or not ap_path:
        raise SystemExit(f'[错误] 未找到微信/支付宝流水（目录 {src_dir}）')

    wx = ae.parse_wechat(wx_path)
    apdf = ae.parse_alipay(ap_path)
    bank_rows, bank_incomes = [], []
    for p in cit_pdfs:
        for r in ae.parse_citic(p):
            if r['支出'] > 0:
                bank_rows.append({'日期': r['日期'], '金额': r['支出'], '明细': r['明细'], '备注': ''})
            if r['收入'] > 0:
                bank_incomes.append({'日期': r['日期'], '金额': r['收入'], '明细': r['明细'], '备注': ''})
    for p in cmb_pdfs:
        for r in ae.parse_cmb(p):
            (bank_incomes if r['金额'] > 0 else bank_rows).append(
                {'日期': r['日期'], '金额': abs(r['金额']), '明细': r['明细'], '备注': ''})
    for p in bank_csvs:
        exp_rows, inc_rows = ae.parse_bank_csv(p)
        bank_rows += exp_rows
        bank_incomes += inc_rows

    wx_exp = wx[wx['收支'] == '支出'].copy()
    ap_exp = apdf[apdf['收支'] == '支出'].copy()
    wx_refund = wx[(wx['收支'] == '收入') & (wx['交易类型'].str.contains('退款', na=False))].copy()
    ap_refund = ae.alipay_refunds(apdf)

    wx_exp['类别'] = wx_exp.apply(ae.map_wechat, axis=1)
    ap_exp['类别'] = ap_exp.apply(ae.map_alipay, axis=1)
    bank_consumed, bank_removed, bank_savings, bank_transfers, bank_internal = ae._bank_split(bank_rows, '银行')

    wx_refund['类别'] = wx_refund.apply(ae.map_wechat, axis=1)
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
                           '对方': [c['明细'] for c in bank_consumed], '商品': '',
                           '金额': [c['金额'] for c in bank_consumed],
                           '类别': [c['类别'] for c in bank_consumed], '备注': '', '单号': ''}) \
        if bank_consumed else pd.DataFrame(columns=['来源', '日期', '对方', '商品', '金额', '类别', '备注', '单号'])
    consume = pd.concat([wx_c, ap_c, bank_c], ignore_index=True)

    reimburse_income, reimburse_rows, _excl = ae.reimburse_income_total(bank_incomes)
    consume, _unabsorbed = ae.net_refunds(consume)
    consume, work_rides, ride_note = ae.extract_work_rides(consume, reimburse_income)

    consume['月份'] = pd.to_datetime(consume['日期'], errors='coerce').dt.strftime('%Y-%m')
    monthly = consume.groupby('月份')['金额'].sum().sort_index()

    return dict(
        consume=consume, monthly=monthly, work_rides=work_rides,
        reimburse_income=reimburse_income, reimburse_rows=reimburse_rows, ride_note=ride_note,
        bank_consumed=bank_consumed, bank_removed=bank_removed, bank_savings=bank_savings,
        bank_transfers=bank_transfers, bank_internal=bank_internal, wx_exp=wx_exp, ap_exp=ap_exp,
    )


def build_json(p, year='2025'):
    ae, consume = p['ae'], p['consume']
    total = round(float(consume['金额'].sum()), 2)
    cat_sum = consume.groupby('类别')['金额'].sum()
    cat_sum_df = cat_sum.reset_index()
    cat_sum_df.columns = ['类别', '金额']
    cat_sum_df['笔数'] = consume.groupby('类别')['金额'].count().reindex(cat_sum_df['类别']).values
    cat_sum_df['占比'] = (cat_sum_df['金额'] / total * 100).round(2)

    monthly = [{'月份': m, '支出': round(float(v), 2)} for m, v in p['monthly'].items()]

    # 主力购物平台（含全品类），与主表口径一致
    plat_all = consume[consume['金额'] > 0].copy()
    plat_all['平台'] = plat_all['对方'].map(ae.platform_of)
    pd_detail = plat_all[plat_all['平台'] != '其他平台']
    psum = pd_detail.groupby('平台')['金额'].agg(['sum', 'count']).reset_index()
    psum.columns = ['平台', '金额', '笔数']
    psum['金额'] = psum['金额'].round(2)
    platform_summary = psum.sort_values('金额', ascending=False).to_dict('records')

    # 加班打车（已剔除，不计入消费）
    wr = p['work_rides']
    workrides = [{'日期': r['日期'], '对方': r['对方'], '金额': round(float(r['金额']), 2)}
                 for _, r in wr.iterrows()] if not wr.empty else []

    reimburse = {
        'total': round(p['reimburse_income'], 2),
        'note': p['ride_note'],
        'lines': [{'日期': r['日期'], '金额': round(float(r['金额']), 2)} for r, _ in p['reimburse_rows']],
    }

    # 明细总览：全消费行 + 平台标签
    detail = []
    for _, r in consume.sort_values('日期').iterrows():
        pl = ae.platform_of(str(r['对方']))
        detail.append({
            '日期': r['日期'], '来源': r['来源'], '对方': r['对方'],
            '类别': r['类别'], '金额': round(float(r['金额']), 2),
            '平台': pl if pl != '其他平台' else None,
        })

    br = pd.DataFrame(p['bank_removed'])
    if not br.empty:
        dedupe = {
            'card': round(float(br[br['明细'].str.contains('信用卡', na=False)]['金额'].sum()), 2),
            'tenpay': round(float(br[br['明细'].str.contains('财付通', na=False)]['金额'].sum()), 2),
            'alipay': round(float(br[br['明细'].str.contains('支付宝', na=False)]['金额'].sum()), 2),
        }
    else:
        dedupe = {'card': 0.0, 'tenpay': 0.0, 'alipay': 0.0}

    bc = pd.DataFrame(p['bank_consumed'])
    bank_direct = []
    if not bc.empty:
        g = bc.groupby('类别')['金额'].agg(['sum', 'count'])
        bank_direct = [{'类别': c, '金额': round(float(row['sum']), 2), '笔数': int(row['count'])}
                       for c, row in g.iterrows()]

    wx_pa = p['wx_exp'].loc[p['wx_exp']['类别'] == '转账往来', '金额'].sum()
    ap_pa = p['ap_exp'].loc[p['ap_exp']['类别'] == '转账往来', '金额'].sum()
    bs = pd.DataFrame(p['bank_savings'])
    bt = pd.DataFrame(p['bank_transfers'])
    bi = pd.DataFrame(p['bank_internal'])
    flows = {
        'savings': round(float(bs['金额'].sum()), 2) if not bs.empty else 0.0,
        'transfer': round(float(bt['金额'].sum() + wx_pa + ap_pa), 2),
        'internal': round(float(bi['金额'].sum()), 2) if not bi.empty else 0.0,
    }

    cats = []
    for _, r in cat_sum_df.iterrows():
        cats.append({'类别': r['类别'], '笔数': int(r['笔数']), '金额': round(float(r['金额']), 2), '占比': float(r['占比'])})

    return {
        'categories': cats,
        'monthly': monthly,
        'platform_summary': platform_summary,
        'workrides': workrides,
        'reimburse': reimburse,
        'detail': detail,
        'meta': {'total': total, 'year': year},
        'flows': flows,
        'dedupe': dedupe,
        'bank_direct': bank_direct,
    }


def inject(template_path, data, out_path):
    with open(template_path, encoding='utf-8') as f:
        html = f.read()
    js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    js = js.replace('</', '<\\/')          # 防止 </script> 提前闭合
    if '/*__DATA__*/null' not in html:
        raise SystemExit('[错误] 模板里没有 DATA 占位符，请确认 ledger_template.html 正确')
    html = html.replace('const DATA = /*__DATA__*/null;', 'const DATA = ' + js + ';')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'[完成] 已生成 {out_path}（{os.path.getsize(out_path):,} 字节）')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input-dir', default=HERE)
    ap.add_argument('--template', default=os.path.join(HERE, 'output', 'ledger_template.html'))
    ap.add_argument('--year', default='2025')
    args = ap.parse_args()

    ae = load_analyzer()
    pipe = run_pipeline(ae, os.path.abspath(args.input_dir))
    pipe['ae'] = ae
    data = build_json(pipe, args.year)
    out = os.path.join(os.path.dirname(args.template), '消费账本-2025.html')
    inject(args.template, data, out)

    json_out = os.path.join(os.path.dirname(args.template), 'ledger_data.json')
    with open(json_out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'[完成] 已生成 {json_out}')
    print(f'[校验] 消费总额 {data["meta"]["total"]:,.2f} 元 · 明细 {len(data["detail"])} 笔 · 平台 {len(data["platform_summary"])} · 加班打车 {len(data["workrides"])} 笔')


if __name__ == '__main__':
    main()
