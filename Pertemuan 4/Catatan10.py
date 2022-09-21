'''
Jika binary search didasarkan pada logika yang berfokus pada bagian tengah data. 
interpolation lebih canggih. Algoritma ini menggunakan nilai target untuk memperkirakan 
posisi elemen dalam array yang diurutkan. Coba memahaminya dengan menggunakan sebuah contoh. 
Asumsikan kita ingin mencari sebuah kata dalam kamus bahasa Inggris, seperti kata ‘river’. 
Kami akan menggunakan informasi ini untuk interpolasi dan mulai mencari kata-kata yang dimulai 
dengan ‘r’.

'''

from interpolationsearch import fungsi_interSearch as fs
from bubblesort import fungsibublesort as fb
list = [12,33,11,99,22,55,90]
sorted_list = fb.Bubblesort(list)

print(fs.Intpolsearch(list,12))
print(fs.Intpolsearch(list,91))

