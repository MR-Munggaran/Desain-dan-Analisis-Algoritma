from binarysearch import fungsiBinarysearch as fbs
from bubblesort import fungsibublesort as bs

list = [12,33,11,99,22,55,90]

sorted_list = bs.Bubblesort(list)

print(fbs.BinarySearch(list,12))
print(fbs.BinarySearch(list,91))