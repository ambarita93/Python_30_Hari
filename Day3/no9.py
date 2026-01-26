import numpy as np
x1=float(input("Enter x_1: "))
y1=float(input("Enter y_1: "))
print("The first coordinate is","(",x1,y1,")")
x2=float(input("Enter x_2: "))
y2=float(input("Enter x_2: "))
print("The second coordinate is","(",x2,y2,")")

slope = (y2-y1)/(x2-x1)
distance = np.sqrt((x2-x1)**2+(y2-y1)**2)

print("The slope of the line is", slope)
print("The distance between the points is",distance)