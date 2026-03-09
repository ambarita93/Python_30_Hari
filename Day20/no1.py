import requests
import webbrowser


url = 'http://www.gutenberg.org/files/1112/1112.txt' # text from a website
response = requests.get(url)
print(response.text[:500]) # print the first 500 characters of the text

url_list = [
    'https://www.python.org','https://www.wikipedia.org','https://www.github.com'
]

for url in url_list:
    webbrowser.open_new_tab(url)
