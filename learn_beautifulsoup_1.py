import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.baidu.com")
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text)
print(soup.head)
print(soup.title)
