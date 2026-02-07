score = float(input("Enter the score: "))

if score>=90 and score <=100:
    print("It gets A grade")
elif score>=80 and score <=89:
    print("It gets B grade")
elif score>=70 and score <=79:
    print("It gets C grade")
elif score>=60 and score <=69:
    print("It gets D grade")
elif score>=0 and score <=59:
    print("It gets E grade")
else:
    print("Please, enter the right score.")



fruit = input("Enter a name of fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_lower = fruit.lower()
if fruit_lower in fruits:
    print("{} exists in the list.".format(fruit_lower))
else:
    print("{} doesn't exists. So,it will be added to the list.".format(fruit_lower))
    fruits.append(fruit_lower)
    print(fruits)
