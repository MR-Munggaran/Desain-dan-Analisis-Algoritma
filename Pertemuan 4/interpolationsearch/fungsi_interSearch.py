def Intpolsearch(list,x):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        #find the mid point
        mid = idx0 + int (((float (idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0])))

        #compare the value at mid point with search value
        if list[mid] == x:
            found = True
            return found
        if list[mid] < x:
            idx0 = mid + 1

    return found