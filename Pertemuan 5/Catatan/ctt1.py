#Hitung Inversi
def countInversion(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                result += 1
    return result



