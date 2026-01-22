'''
Program menghitung jarak dua titik dengan metode Euclidean Distance
'''
import math
titik1 = [0,0]
titik2 = [10,0]

jarak = math.sqrt((titik2[0]-titik1[0])**2+(titik2[1]-titik1[1])**2)
print(jarak)