

df2 = pd.read_csv('weight-height.csv')
print(df2.head()) # menampilkan 5 baris pertama dari sebuah tabel
print(df2.tail()) # menampilkan 5 baris terakhir dari sebuah tabel
tinggi = df2['Height']
print(tinggi.describe())
massa = df2['Weight']
