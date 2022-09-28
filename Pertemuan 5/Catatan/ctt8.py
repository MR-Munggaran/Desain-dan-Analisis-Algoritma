#Mencari nilai terdekat dengan metode devide dan conquer

from email.errors import CloseBoundaryNotFoundDefect


def closestNumber(arr,low,high,x):
    if low>high:
        return -1
    if arr[high]<= x:
        return arr[high]
    if arr[low] >= [low]:
        return arr[low]
    
    mid = (low+high) // 2

    if arr[mid] == x:
        return arr[mid]
    
    abs_mid = abs(arr[mid]-x)

    if mid > 0:
        abs_left = abs(arr[mid-1]-x)
        if abs_left<abs_mid:
            return closestNumber(arr,low,mid-1,x)
    
    if mid < high:
        abs_right = abs(arr[mid+1]-x)
        if abs_right < abs_mid:
            return closestNumber(arr,mid+1,high,x)
    #print("after")
    return arr[mid]



