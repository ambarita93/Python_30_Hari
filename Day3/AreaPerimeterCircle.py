import numpy as np
radius = float(input("Enter radius: "))
area  = np.pi * radius**2
circumference = 2 * np.pi *radius

print("Area of circle is", area," and it's circumference is ",circumference)