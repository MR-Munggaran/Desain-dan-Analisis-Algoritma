list = [25,21,22,24,23,27,26]

#modifikasi sesuai angka favorit anda

lastElementIndex = len(list)-1
print(0,list)
for i in range(lastElementIndex):
    if list[i] > list[i+1]:
        list[i], list[i+1] = list[i+1], list[i]
    print(i+1, list)

