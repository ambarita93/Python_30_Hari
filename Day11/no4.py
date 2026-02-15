def print_list(*my_list):
    for item in my_list:
        print(item)

def reverse_list(*my_list2):
    for item in reversed(my_list2):
        print(item)

def capitalize_list_items(*mylist3):
    capital_list = []
    for item in mylist3:
        capital_list.append(item.upper())
    return capital_list

def add_item(mylist,item):

    mylist.append(item)
    return mylist

numbers = [1,2,3,4,4,5,6]

print(add_item(numbers,'23'))

