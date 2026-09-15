# Filtering : Refers to the process of selecting elements from an array that match a given condition

import numpy as np

ages = np.array([[21 , 17 , 19 , 20 , 16 , 30 , 18  , 65],
                 [39 , 33 , 15 , 99 , 18 , 19 , 20 , 21]])

# Boolean indexing (fast)
# This will flatten the array , array will not is original shape
teenagers = ages[ages < 18]
print(teenagers) # [17 16 15] (Flatten the array to 1-D)

adults = ages[(ages >= 18) & (ages <= 65)] # not write "and" insted use "&" that is and operator in numpy
print(adults) # [21 19 20 30 18 65 39 33 18 19 20 21]

seniors = ages[ages >= 65]
print(seniors) # [65 99]

evenAge = ages[ages % 2 == 0]
print(evenAge) # [20 16 30 18 18 20]

oddAge = ages[ages % 2 == 1]
print(oddAge) # [21 17 19 65 39 33 15 99 19 21]

print("*" * 50)

# This will preseve the original shape of the array
# np.where(condition , array name , value if condition not satisfy (0,-1,np.nan))
# this is slower than boolean indexing
adult = np.where((ages >= 18) & (ages <= 65) , ages , 0)
print(adult)
#[[21  0 19 20  0 30 18 65]
# [39 33  0  0 18 19 20 21]]

print("*" * 50)

#Exercise :

arr = np.array([-3, 5, -1, 8, 0, -7, 2])
print(arr[arr < 0]) # [-3 -1 -7]
print(arr[(arr > 0) & (arr < 5)]) # [2]

arr = np.array([[10, 20, 30],
                [5, 15, 25],
                [40, 50, 60]])
#Filter rows where first column > 10
print(arr[: , 0] > 10) # [False False  True]
res = arr[: , 0] > 10
result_Row = arr[res]
print(result_Row) # [[40 50 60]]
