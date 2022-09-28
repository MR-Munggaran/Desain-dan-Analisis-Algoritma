#tanpa devide dan conquer
def maxSubSum(arr):
    MaxCon = 0
    MaxEnd=0

    for i in range(len(arr)):
        MaxEnd += arr[i]
        if MaxEnd > MaxCon:
            MaxCon = MaxEnd
        if MaxEnd<0:
            MaxEnd=0
    return MaxCon


