bilangan = int(input("masukan bilangan : "))
pangkat = int(input("masukan pangkat : "))

def hitungpangkat(bilangan,pangkat):
    if pangkat > 1:
        return bilangan * hitungpangkat(bilangan,pangkat - 1)
    return bilangan 

hasil = hitungpangkat(bilangan, pangkat)
print(f"Hasil = {hasil}")

