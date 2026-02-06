# no.1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need {} more year(s) to learn drive.'.format(18-age))

#no.2
your_age = int(input('Enter your age: '))
my_age = 33

if (your_age-my_age)>1:
    print('You are {} years older than me.'.format(your_age-my_age))
elif (your_age-my_age)==1:
    print('You are {} years older than me.'.format(your_age-my_age))
elif (your_age-my_age) ==-1:
    print('You are {} year younger than me.'.format(my_age-your_age))
elif (your_age-my_age) ==0:
    print('We are the same age')
else: 
    print('You are {} years younger than me.'.format(my_age-your_age))

#no.3
number1 = int(input('Enter number one: '))
number2 = int(input('Enter number two: '))

if number1>number2:
    print('Number {} is greater than {}.'.format(number1,number2))
elif number1<number2:
    print('Number {} is smaller than {}.'.format(number1,number2))
else:
    print('The numbers are equal.')