numbers =  [i for i in range(20)]

def is_odd(number):
    if number%2 !=0:
        return True
    return False

odd_numbers = filter(is_odd,numbers)
print(list(odd_numbers))


def cubic(number):
    return number**3

numbers_cubic = map(cubic,numbers)
print(list(numbers_cubic))