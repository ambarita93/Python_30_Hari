import requests

from bs4 import BeautifulSoup

url = 'https://www.kompas.com/'

response = requests.get(url)
status = response.status_code
print(status)

