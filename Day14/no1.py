numbers =  [i for i in range(30)]

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

def quant_number(number):
    return number**4
numbers_quant = map(quant_number,numbers)
print(list(numbers_quant))