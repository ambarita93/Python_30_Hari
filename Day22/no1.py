import requests

from bs4 import BeautifulSoup

url = 'https://archieve.ics.uci.edu/ml/dataset.php'

response = requests.get(url)
status = response.status_code

if status == 200:
    soup = BeautifulSoup(response.text, 'html.parser')