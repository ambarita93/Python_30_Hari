import requests

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
status = response.status_code
print(status)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
#print(soup.title.get_text())
print(soup.body)

tables = soup.find_all('table',{'cellpadding':'10'})
tables = tables[0]
print(tables)
