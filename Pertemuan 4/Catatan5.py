from insertionsort import fungsiInsertionSort as fis

list = [25,26,22,24,27,23,21]
out = fis.insertion(list)
print(out)


'''
Jika struktur data sudah diurutkan, 
insertion sort akan berjalan dengan sangat cepat. 
Bahkan, jika struktur data diurutkan, 
maka insertion sort akan memiliki waktu berjalan linier; yaitu, O(n). 
Worst case adalah saat setiap loop dalam harus memindahkan semua elemen dalam list. 
Jika loop dalam ditentukan oleh i, performa terburuk dari algorita insertion sort diberikan
sebagai berikut:


Secara umum, insertion dapat digunakan pada struktur data kecil. 
Untuk struktur data yang lebih besar, insertion sort tidak disarankan karena 
performa rata-rata kuadratiknya.

'''