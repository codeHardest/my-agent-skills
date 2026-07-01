import requests, json, datetime
url = 'https://api.bilibili.com/x/web-interface/view?bvid=BV1Q4EL6yEZL'
headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.bilibili.com'}
data = requests.get(url, headers=headers).json()
info = data['data']

# Write the title to a separate file with explicit utf-8 (avoid console garbled output)
with open('./downloads/bilibili/BV1Q4EL6yEZL/_title.txt', 'w', encoding='utf-8') as f:
    f.write(info['title'])

# Save full info
with open('./downloads/bilibili/BV1Q4EL6yEZL/_info.json', 'w', encoding='utf-8') as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

pubdate_ts = info['pubdate']
pubdate = datetime.datetime.fromtimestamp(pubdate_ts).strftime('%Y-%m-%d')

# Write metadata for use by other scripts
with open('./downloads/bilibili/BV1Q4EL6yEZL/_meta.txt', 'w', encoding='utf-8') as f:
    f.write(f"AID={info['aid']}\n")
    f.write(f"CID={info['cid']}\n")
    f.write(f"DURATION={info['duration']}\n")
    f.write(f"PUBDATE={pubdate}\n")
    f.write(f"OWNER={info['owner']['name']}\n")

print("done")
