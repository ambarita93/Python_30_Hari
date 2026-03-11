import requests
import statistics

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
data_of_cat = response.json()

life_span = []
for data in data_of_cat:
    life_span.append(data['life_span'])

life_span_min = []
life_span_max = []
life_span_median = []

for data in life_span:
    min_data = float(data[0])
    max_data = float(data[-1])
    median_data = (min_data+max_data)/2
    life_span_min.append(min_data)
    life_span_max.append(max_data)
    life_span_median.append(median_data)

max_life_span = max(life_span_max)
min_life_span = min(life_span_min)
median_life_span = statistics.median(life_span_median)
std_life_span = statistics.stdev(life_span_median)
print(f"The highest lifes span is {max_life_span}, the shortest is {min_life_span}, the median is {median_life_span}, and standard deviation of cats' life span {std_life_span}")

