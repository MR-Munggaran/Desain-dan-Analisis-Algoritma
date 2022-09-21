def Bubblesort(list):
#exchange the element to arrange in order
    lastElementIndex = len(list)-1
    for passno in range(lastElementIndex,0,-1):
        for i in range(passno):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

