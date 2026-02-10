for i in range(101):
    if i%2==0:
        print(i)
    else:
        continue

for i in range(101):
    if i%2==0:
        continue
    else:
        print(i)

total=0
for i in range(101):
    total = total + i
print("The sum of all numbers is",total)
even_total = 0

for i in range(101):
    if i%2==0:
        even_total = even_total + i
    else:
        continue
odd_total = total - even_total
print('The sum of all even numbers is {} and the sum of all odd number is {}.'.format(even_total, odd_total))