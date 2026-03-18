import requests

from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Provinces_of_Indonesia'

headers_saya = {'User-Agent': 'LearnScraping/1.0 (handyambarita@gmail.com)'}
response = requests.get(url, headers=headers_saya)
status_code = response.status_code

print(f"Kode Status: {status_code}")

soup = BeautifulSoup(response.content, 'html.parser')
tabel_provinsi = soup.find('table', {'class': 'sortable'}) # ambil tabel dari class sortable

if tabel_provinsi: # tabel tidak kosong
    semua_baris = tabel_provinsi.find_all('tr')
    data_hasil_scraping = []

    for baris in semua_baris:
        kolom = baris.find_all('td')
        if len(kolom)>7:
            nama_provinsi = kolom[4].get_text(strip=True)
            luas_wilayah = kolom[7].get_text(strip=True)
            populasi = kolom[8].get_text(strip=True)
            data_hasil_scraping.append({
                'Provinsi': nama_provinsi,
                'Luas': luas_wilayah,
                'Populasi':populasi
            })
    print("\nScraping selesai.")
else: #tabel kosong
    print("Tabel provinsi tidak ditemukan.")
print(data_hasil_scraping)

