import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv
import json

# 웹 페이지에서 데이터 가져오기
response = requests.get('https://paullab.co.kr/stock.html')
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 데이터 추출하기
twoStep = soup.select('.main')[2].select(' tbody > tr')[1:]
날짜 = []
종가 = []
전일비 = []
거래량 = []

for i in twoStep:
    날짜.append(i.select('td')[0].text)
    종가.append(int(i.select('td')[1].text.replace(',', '')))
    전일비.append(int(i.select('td')[2].text.replace(',', '')))
    거래량.append(int(i.select('td')[6].text.replace(',', '')))

# 데이터를 딕셔너리 형태로 저장하기
l = []
for i in range(len(날짜)):
    l.append({
        '날짜': 날짜[i],
        '종가': 종가[i],
        '전일비': 전일비[i],
        '거래량': 거래량[i],
    })

# 그래프 그리기
plt.plot(날짜, 종가)
plt.xticks(rotation=-45)
plt.show()

# JSON 파일로 저장하기
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
  json.dump(l, f_write, ensure_ascii=False, indent=4)

# JSON 파일에 변수명 추가하기
data = ""
with open('data.js', "r", encoding="UTF-8-sig") as f:
  line = f.readline()
  while line:
    data += line
    line = f.readline()

final_data = f"var data = {data};"
with open('data.js', "w", encoding="UTF-8-sig") as f_write:
  f_write.write(final_data)
