def is_prime(number):
    if isinstance(number,int):
        if number==2 or number==3:
            print(f"{number} is prime number.")
        elif number==1:
            print(f"{number} is not prime.")
        else:
            for i in range(2,number):
                if number%i == 0:
                    return print(f"{number} is not prime.")
                    break
                elif i+1 == number:
                    return print(f"{number} is prime.")
                else:
                    continue
        
    else:
        print("Enter an integer.")



for i in range(1,100000):
    is_prime(i)