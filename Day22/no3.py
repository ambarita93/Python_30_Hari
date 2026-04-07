import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
status = response.status_code
print(status)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())