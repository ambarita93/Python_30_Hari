from datetime import datetime

sekarang = datetime.now()

hari = sekarang.day
bulan =  sekarang.month
cap_waktu = sekarang.timestamp()

print(hari,bulan,cap_waktu)