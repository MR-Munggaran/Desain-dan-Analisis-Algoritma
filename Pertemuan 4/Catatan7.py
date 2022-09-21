'''
Performa terburuk dari sort selection adalah O(n2). 
Perhatikan bahwa kinerja terburuknya mirip dengan bubble sort dan 
tidak boleh digunakan untuk menyortir kumpulan data yang lebih besar. 
Namun, selection sort adalah algoritma yang dirancang lebih baik daripada 
bubble sort dan kinerja rata-ratanya lebih baik daripada bubble sort karena 
pengurangan jumlah penukarannya.

'''

from selectionsort import fungsiSelectionSort as fss

list = [70,15,25,19,34,44]

out = fss.selection(list)

print(out)