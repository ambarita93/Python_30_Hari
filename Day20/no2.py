import requests

url = 'https://api.thecatapi.com/v1/breeds' # berikan nama website
response = requests.get(url) # akses website
print(response) # tampilkan apakah websitenya memberi respons yang diharapkan
data_of_cat = response.json() #ambil data yang semula JSON kemudian dijadikan list 

print(data_of_cat[:1]) #tampilkan data pertama.

for data in data_of_cat: # ambil data weight dari data_of_cat
    wht = data['weight']
    nam = data['name']
    print(nam,wht)
