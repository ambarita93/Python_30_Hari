import json
import requests

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/East_Java'
header_saya = {'User-Agent': 'LearnScraping2/1.0 (handyambarita@gmail.com)'}
response = requests.get(url,headers=header_saya)
status_code = response.status_code

soup = BeautifulSoup(response.content,'html.parser')
tabel_kabupaten = soup.find('table',{'class':'sortable'})