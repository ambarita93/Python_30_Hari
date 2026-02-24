numbers = [3,2,4,5]

def square(x):
    return x**2

squares_numbered = map(square,numbers)

def is_prime(x):
    for i in range(1,9):
        if x%i ==0:
            mark = mark + 1
        else:
            continue

def add_two_numbers(x,y):
    return x * y

from functools import reduce

total = reduce(add_two_numbers,numbers)

print(total)