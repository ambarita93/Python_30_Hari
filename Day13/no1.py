#learn list comprehension

numbers = [i for i in range(100)]
squared_numbers = [i*i for i in range(11)]
print(squared_numbers)

coordinate = [(i,i**2) for i in range(15)]


even_numbers = [i for i in range(100) if i%2==0]

squares = lambda x:x**2
print(squares(5))

cubics = lambda x:x**3
print(cubics(5))

function2 = lambda a,b,c:c**a-b
print(function2(1,2,3))

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [i for i in numbers if i>0]
print(filtered_numbers)

something = [(i,j,k) for i in range(2) for k in range(3) for j in range(4)]
print(something)