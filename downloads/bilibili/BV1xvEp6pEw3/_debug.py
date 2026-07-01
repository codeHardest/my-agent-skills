import requests
url = 'https://api.bilibili.com/x/web-interface/view?bvid=BV1xvEp6pEw3'
headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.bilibili.com'}
r = requests.get(url, headers=headers)
raw = r.content
# Find the start of title content
start = raw.find(b'"title":"') + len(b'"title":"')
end = raw.find(b'",', start)
title_bytes = raw[start:end]
print('First 30 bytes hex:', title_bytes[:30].hex())
print('---')
for enc in ['utf-8', 'gbk', 'gb2312', 'big5', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin1']:
    try:
        decoded = title_bytes.decode(enc)
        print(f'{enc}: {decoded[:80]}')
    except Exception as e:
        print(f'{enc}: FAILED - {e}')
