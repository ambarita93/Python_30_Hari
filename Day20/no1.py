import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

respons = requests.get(url)
print(respons)
