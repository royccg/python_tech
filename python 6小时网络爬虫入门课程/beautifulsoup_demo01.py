from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
print(soup.a.name)
tag = soup.a
print(tag.attrs)
print(soup.a)
