def check_season(month):
    Autumn = ['september','october','november']
    Winter = ['december','january','february']
    Spring = ['march','april','may']
    Summer = ['june','july','august']
    print(f"You enter {month}.")
    if month.lower() in Autumn:
        print(f"The season of {month} is Autumn.")
    elif month.lower() in Winter:
        print(f"The season of {month} is Winter.")
    elif month.lower() in Spring:
        print(f"The season of {month} is Spring.")
    elif month.lower() in Summer:
        print(f"The season of {month} is Summer.")
    else:
        print("Please input a correct month!")


check_season('april')

import math

def solve_quadratic_eqn():
    print("Equation of quadratic of form ax^2+bx+c=0")
    a = float(input("Enter x^2 coeficient: "))
    b = float(input("Enter x coeficient: "))
    c = float(input("Enter constant: "))
    print("your equation is {}x^2+b{}+c=0.".format(a,b,c))
    
    D = b**2-4*a*c
    if D==0:
        solution = -1*b/(2*a)
        print(f"The solution: {solution}")
    elif D>0:
        solution1 = (-1*b+math.sqrt(D))/(2*a)
        solution2 = (-1*b-math.sqrt(D))/(2*a)
        print(f"The solutions: {solution1} and {solution2}")
    else:
        print(f"Nothing because the discriminant is negative ({D})")

solve_quadratic_eqn()