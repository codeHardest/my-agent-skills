import requests, json
url = 'https://api.bilibili.com/x/web-interface/view?bvid=BV1xvEp6pEw3'
headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.bilibili.com'}
r = requests.get(url, headers=headers)
data = r.json()
info = data['data']

# Write the title to a separate file with explicit utf-8
with open('./downloads/bilibili/BV1xvEp6pEw3/_title.txt', 'w', encoding='utf-8') as f:
    f.write(info['title'])

# Save full info
with open('./downloads/bilibili/BV1xvEp6pEw3/_info.json', 'w', encoding='utf-8') as f:
    json.dump(info, f, ensure_ascii=False, indent=2)

print("title bytes:", info['title'].encode('utf-8')[:50])
print("done")
