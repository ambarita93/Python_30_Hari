import requests

url = 'https://www.gutenberg.org/files/1342/1342-0.txt' # text from a website
response = requests.get(url)
print(response.text[:500]) # print the first 500 characters of the text