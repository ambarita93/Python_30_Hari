try:
    name = input("Enter your name: ")
    year_born = input("Year you were born: ")
    age = 2019 - year_born
    print(f"You are {name}. Your age is {age}.")
except:
    print("Someting went wrong.")
finally:
    print("Terima kasih")