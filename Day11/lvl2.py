def evens_and_odds(number):
    mark_odd = 0
    mark_even = 0
    for i in range(number):
        if i%2==0:
            mark_even = mark_even +1
        else:
            mark_odd = mark_odd + 1
    return print(f"The number of odds are {mark_odd} and the number of even are {mark_even}")

evens_and_odds(100)

def factorial(number):
    '''
    Docstring for factorial
    Return the value of n! (n factorial). 
    :param number: whole number. it can be a negative number.
    '''
    if number==1 or number==0:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(10))


def unique_list(*lst):
    n = len(lst)
    mark =0
    not_unique = []
    for i in range(n-1):
        if lst[i] == lst[i+1]:
            mark = mark + 1
            not_unique.append(lst[i])
        else:
            continue
    if mark == 0:
        return print(f"List {lst} are unique!")
    else:
        return print(f"List {lst} are not unique! The item:{not_unique} appear more than once.")

unique_list(1,2,18,3,4,5,6,7,8,9,17,12,13,'a','b','c')