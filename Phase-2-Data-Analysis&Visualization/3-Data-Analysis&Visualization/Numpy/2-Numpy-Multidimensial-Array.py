import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])

print(type(arr)) #ndarray -> n dimensial array
print(arr)
print(arr[0][0]) #-> 0 row , 0 column -> 1
print(arr[1][2]) #-> 1 row , 2 column -> 6

alpha = np.array([
    ["A" , "B" , "C" , "D" , "E"],
    ["F" , "G" , "H" , "I" , "J"],
    ["K" , "L" , "M" , "N" , "O"],
    ["P" , "Q" , "R" , "S" , "T"],
    ["U" , "V" , "W" , "X" , "Y"]
])

print(alpha[1][2] + alpha[0][4] + alpha[3][4]) # -> HET
print(alpha[1,2] + alpha[0,4] + alpha[3,4]) # -> HET
