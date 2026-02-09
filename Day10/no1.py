for i in range(1,11):
    print("'for'",i)

k=1
while k <= 10:
    print("'while'",k)
    k = k + 1

for j in range(10,0,-1):
    print("'for'",j)

s = 10
while s>0:
    print("'while'",s)
    s = s - 1

for i1 in range(8):
    for i2 in range(0,i1):
        print('#',end='')
    print("")
print('\n')

for i1 in range(9):
    for i2 in range(9):
        print("#",end=' ')
    print("")
