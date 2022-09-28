#PROGRAM UTAMA


#Catatan 1
#====================================
from Catatan import ctt1 as ct1
arr = [21,70,36,14,25]
print(ct1.countInversion(arr))


#Catatan 2
#=====================================
from Catatan import ctt2 as ct2
arr = [1,20,6,4,5]
print(ct2.countInversion(arr))


#Catatan 3
#=====================================
from Catatan import ctt3 as ct3
arr = [-2,-5,6,-2,-3,1,5,-6]
print(ct3.maxSubSum(arr=arr))


#Catatan 4
#=====================================
from Catatan import ctt4 as ct4
arr = [-2,-5,6,-2,-3,1,5,-6]
print(ct4.maxSum(arr,0,len(arr)-1))


#Catatan 5
#=====================================
from Catatan import ctt5 as ct5
arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
akhir = ct5.longestCommonPrefix(arr, 0, len(arr)-1)
print(akhir)


#Catatan 6
#=====================================
from Catatan import ctt6 as ct6
arr = [1,11,15,26,38]    
arr1 = [2,13,17,30,45]    
print(ct6.medianOfArray(arr,arr1,len(arr)))


#Catatan 7
#=====================================
from Catatan import ctt7 as ct7
arr = [1,2,8,10,12,14,19]
x = 5
print(ct7.floorSorted(arr,0,len(arr)-1))
#Catatan 8
#=====================================
from Catatan import ctt8 as ct8
arr = [2,5,6,7,8,8,9]
x = 9
print(ct8.closestNumber(arr,0,len(arr)-1,x))
#Catatan 9
#=====================================
from Catatan import ctt9 as ct9
arr = [9,1,4,5,2]
print(ct9.fixedPoint(arr,0,len(arr)-1))

