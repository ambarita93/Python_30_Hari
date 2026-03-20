import json
import requests

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/East_Java'
header_saya = {'User-Agent': 'LearnScraping2/1.0 (handyambarita@gmail.com)'}
response = requests.get(url,headers=header_saya)
status_code = response.status_code

soup = BeautifulSoup(response.content,'html.parser')
tabel_kabupaten = soup.find('table',{'class':'sortable'})
if tabel_kabupaten:
    semua_baris = tabel_kabupaten.find_all('tr')
    data_hasil_scraping = []

    for baris in semua_baris:
        kolom = baris.find_all('td')
        if len(kolom)>7:
            nama_kabupaten_kota = kolom[1].get_text(strip=True)
            hd_index = kolom[-1].get_text(strip=True)
            print(f"Region {nama_kabupaten_kota} and its HD Index: {hd_index}")