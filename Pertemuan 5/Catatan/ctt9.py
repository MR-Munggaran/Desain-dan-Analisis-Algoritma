#mencari fixed point dengan metode devided dan conquer

def fixedPoint(arr,low,high):
    if low>high:
        return -1
    
    if arr[high] == high:
        return arr[high]
    
    if arr[low] == low:
        return arr[low]
    
    mid = (low+high) // 2

    if arr[mid] == mid:
        return arr[mid]
    
    if mid > arr [mid]:
        return fixedPoint(arr,mid+1,high)
    else:
        return fixedPoint(arr,low,mid-1)

