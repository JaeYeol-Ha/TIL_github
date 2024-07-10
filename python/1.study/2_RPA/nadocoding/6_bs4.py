import requests
from bs4 import BeautifulSoup

# url = "https://battlecats-db.com/unit/r_ssr.html"
url = "https://comic.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Whale/2.11.126.19 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
print(soup.a)
print(soup.a.attrs)