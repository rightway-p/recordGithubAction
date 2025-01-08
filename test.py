import requests
from bs4 import BeautifulSoup

#url = 'https://ridibooks.com/category/bestsellers/2200'
url = 'https://paullab.co.kr/stock.html'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.date')
for no, book in enumerate(bookservices, 1):
  print(no, book.text.strip())
