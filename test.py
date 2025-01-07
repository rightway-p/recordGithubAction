import requests
from bs4 import BeautifulSoup

print('111')
url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
print('html: ', html)
soup = BeautifulSoup(html, 'html.parser')
print('soup: ', soup)

bookservices = soup.select('.title_text')
for no, book in enumerate(bookservices, 1):
  print(no, book.text.strip())
  print('222')
