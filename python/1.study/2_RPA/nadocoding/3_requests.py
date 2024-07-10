import requests

url = "https://battlecats-db.com/unit/r_ssr.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Whale/2.11.126.19 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("battlecats_ssr.html","w", encoding="utf-8") as f:
    f.write(res.text)

print("웹 스크래핑 진행 완료.")