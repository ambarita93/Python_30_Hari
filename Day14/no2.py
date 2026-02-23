numbers = [1,2,3,4,5,6]

def square(x):
    return x**2

squares_numbered = map(square,numbers)

def is_prime(x):
    for i in range(1,9):
        if x%i ==0:
            mark = mark + 1
        else:
            continue
        