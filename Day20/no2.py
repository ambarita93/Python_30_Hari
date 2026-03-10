import requests
import statistics

url = 'https://api.thecatapi.com/v1/breeds' # berikan nama website
response = requests.get(url) # akses website
print(response) # tampilkan apakah websitenya memberi respons yang diharapkan
data_of_cat = response.json() #ambil data yang semula JSON kemudian dijadikan list 

#print(data_of_cat[:1]) #tampilkan data pertama dari data_of_cat.


wht = []
for data in data_of_cat: # ambil data weight dari data_of_cat untuk ditaruh di list wht. data_of_cat adalah list yang berisi dictionary.
    wht.append(data['weight'])
wht_metric_min = []
wht_metric_max = []
wht_metric_median = []
for data in wht:
    min_data = float(data['metric'][0])
    max_data = float(data['metric'][-1])
    median_data = (min_data+max_data)/2
    wht_metric_min.append(min_data)
    wht_metric_max.append(max_data)
    wht_metric_median.append(median_data)


max_weight = max(wht_metric_max)
min_weight = max(wht_metric_min)
median_weight = statistics.median(wht_metric_median)
std_weight = statistics.stdev(wht_metric_median)    
print(f"The biggest weight is {max_weight}, the lightest is {min_weight}, the median {median_weight}, and standard deviation of cats' weight {std_weight}")
