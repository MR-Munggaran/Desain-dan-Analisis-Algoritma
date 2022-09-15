import datetime as dt
harini = dt.datetime(2022,9,14)
today = (harini.strftime("%d/%m/%Y")) 


Mahasiswa = ["Muhammad Rafi Munggaran", 2021071028, "Informatika", "Desain dan analisis algoritma",today, "UPJ"]

for i in Mahasiswa:
    print(f" UPJ :{i}")