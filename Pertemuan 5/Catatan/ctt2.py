#Hitung inversi dengan divide dan conquer
from array import array


def countInversion(arr:array): 
    icount  = 0

    if len(arr) <= 1:
        return icount

    mid     = len(arr) // 2
    left    = arr[:mid]
    right   = arr[mid:]
    icount  += countInversion(left)
    icount  += countInversion(right)
    i=j=k   = 0

    #print(left)
    #print(right)

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr [k] = left[i]
            i+= 1
        else:
            #print(left[i], right [j])
            arr[k] = right[j]
            j+=1
            icount += (mid-i)
        k+=1

    while i<len(left):
        arr[k] = left[i]
        i+=1
        k+=1
    
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    
    return icount


