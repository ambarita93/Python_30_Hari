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
print(df)

df2 = pd.read_csv('weight-height.csv')
print(df2.head()) # menampilkan 5 baris pertama dari sebuah tabel
print(df2.tail()) # menampilkan 5 baris terakhir dari sebuah tabel
tinggi = df2['Height']
print(tinggi.describe())
massa = df2['Weight']
bobot = [74,78,69]

df['Masssa'] = bobot

print(df)
