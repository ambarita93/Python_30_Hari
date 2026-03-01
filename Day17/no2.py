#learn to use unpack and pack Mar 1 '2026



def sum_of_five_nums(a,b,c,d,e):
    return a+b+c+d+e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))

numbers = range(2,7)
print(list(numbers))

# now use unpack method to make a list.

args =  [2,7]
numbers = range(*args)
print(list(numbers))

# unpacking dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year(s) old.'

data = {'name':'Handy', 'country':'Indonesia','city':'Surabaya','age':33}

print(unpacking_person_info(**data))

#packing dictionaries
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key}={kwargs[key]}")
    return kwargs

print(packing_person_info(name='Handy Ambarita',country ='Indonesia',city='Surabaya',age = '33'))

# learn to use enumerate
for index, item in enumerate([20,30,40,50,55,65,79]):
    print(index,item)

countries = ['Finland','Indonesia','Sweden','Germany','Norway','Denmark','Iceland']
for index, item in enumerate(countries):
    if item == 'Indonesia':
        print(f'The country {item} has been found at index {index}')
# learn to use zip
# sometimes we would like to combine list when looping through them. 

fruits = ['apple','banana','mango','orange','pineapple','watermelon']
vegetables = ['tomato','potato','cabbage','onion','carrot','ginger']
fruits_and_vegetables = [] # combine fruits and vegetables
for f,v in zip(fruits,vegetables):
    fruits_and_vegetables.append({'fruit':f,'veg':v})

print(fruits_and_vegetables)