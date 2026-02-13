import numpy as np
import numbers

def add_two_numbers(number1,number2):
    sum_two_numbers = number1+number2
    return sum_two_numbers

def area_of_circle(radius):
    area = np.pi * radius ** 2
    return area

def add_all_nums(*numbers):
    total = 0
    print('you input {}'.format(numbers))
    for number in numbers:
        if isinstance(number,(int,float)):
            total = total + number
        else:
            print('{} is not a number'.format(number))
    return total

print(add_all_nums(1,2,3,4,5,'a','b'))

def convert_celcius_to_fahrenheit(temperature):
    print('You input {} Celcius'.format(temperature))
    temp_in_fahreiheit = (temperature*9/5)+32
    return temp_in_fahreiheit

print(convert_celcius_to_fahrenheit(0))