def LiniearSearch (list, item):
    index = 0
    found = False

    #match the value with each data element
    while index < len(list) and found is False:
        if list[index] == item:
            found = True
        else:
            index = index + 1

    return found