import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.children)

"""
test=list(soup.children)
for i in test:
    print(" = ",i)
print("=======")
html = list(soup.children)[2]
print(list(html.children))
print("=======")
body = list(html.children)[3]
print(list(body.children))
print("=======")
p = list(html.children)[1]
print(list(p.children))
print(p.get_text())
"""

"""
#print(soup.find_all('p'))
print(soup.find_all('p')[0].get_text())                     #Tìm tất cả thẻ p
print(soup.find('p'))                                       #Tìm thẻ p đầu tiên
"""