import pandas as pd
import numpy as np

fruits = ['Orange','Mango','Banana']
s = pd.Series(fruits)
print(s)

nums = [1,2,3,4,5,6,7]
s10 = pd.Series(10,index=[1,2,3,4,5])
print(s10)

data = [['Handy','Indonesia','Surabaya'],
        ['Mateo','Rusia','Moskow'],
        ['Ambarita','Belanda','Amsterdam']
        ]
df = pd.DataFrame(data,columns=['Nama','Negara','Kota'])

bobot = [74,78,69]
tinggi2 = [163,175,160]

df['Masssa'] = bobot
df['Tinggi'] = tinggi2
print(df)
