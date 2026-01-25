print("Given y=2x-2. Find slope,x-intercept, and y-intercept of the line.")
x_1 = float(input("Enter x_1: "))
y_1 = 2*x_1-2
print("Coordinate is","(",x_1,y_1,")" )
x_2 = float(input("Enter x_2: "))
y_2 = 2*x_2-2
print("Coordinate is","(",x_2,y_2,")" )
slope = (y_2-y_1)/(x_2-x_1)
print("The slope of the line is ",slope)
x_intercept = (0+2)/2
print("x-intercept of line is ","(",x_intercept,0,")")
y_intercept = 2*0-2
print("x-intercept of line is ","(",0,y_intercept,")")