import csv
import requests
from bs4 import BeautifulSoup

url = "https://battlecats-db.com/unit/status_r_ssr.html" 

filename = "battlecats.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)

title = "No.    랭크	캐릭터 이름	CustomizeLv	체력	KB	속도	공격력	DPS	범위	빈도 F	발생 F  사거리  비용    재생산  특성".split("\t")
writer.writerow(title)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"ssList"}).find("tbody").find_all("tr")
print(type(data_rows))
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns]
    # print(data)
    writer.writerow(data)
