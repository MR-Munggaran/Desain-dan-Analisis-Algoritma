import pandas as pd 

df = pd.DataFrame([
    ['1','Informatika', 50,30,20],
    ['2', 'Sistem Informasi',55,30,25],
    ['3', 'Teknik Sipil',40,30,10]
])
df.columns = ['No', 'Prodi','Mahasiswa','Laki - laki', 'perempuan']
print(df)