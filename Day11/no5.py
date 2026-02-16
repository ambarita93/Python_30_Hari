def remove_item(mylist,item):
    mylist.remove(item)
    return mylist


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff,'Potato'))


def sum_of_numbers(numbers):
    total = 0
    for i in range(numbers+1):
        total = total + i
    return total

print(sum_of_numbers(1000))

def sum_of_odds(numbers):
    total = 0
    for i in range(numbers+1):
        if i%2 !=0:
            total = total + i
        else:
            continue
    return total

print(sum_of_odds(1000)) 

def sum_of_evens(numbers):
    total = 0
    for i in range(numbers+1):
        if i%2 ==0:
            total = total + i
        else:
            continue
    return total

print(sum_of_evens(1000)) 
