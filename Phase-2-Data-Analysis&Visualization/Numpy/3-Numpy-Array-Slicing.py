import numpy as np

arr = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# Slicing -> array_name[start : end : step]

print(arr) # whole arr

# row wise
print(arr[0]) # [1,2,3,4] -> only o row
print(arr[1:3]) # [[ 5  6  7  8] [ 9 10 11 12]] -> 1 to 3
print(arr[2::]) # [[ 9 10 11 12] [13 14 15 16]] -> 2 to end
print(arr[:2:]) # [[1 2 3 4] [5 6 7 8]] -> start to 2
print(arr[::2]) # [[ 1  2  3  4] [ 9 10 11 12]] -> 0 2 4 6 step wise
print(arr[::-1]) # [[13 14 15 16] [ 9 10 11 12] [ 5  6  7  8] [ 1  2  3  4]] -> end to start reverse
print(arr[::-2]) # [[13 14 15 16] [ 5  6  7  8]] -> end to start but with 2 step

# column wise
print(arr[: , 0]) # [ 1  5  9 13] -> first column
print(arr[: , -1])  # [ 4  8 12 16] -> last column
print(arr[: , 1:3]) # [ 2  3] [ 6  7] [10 11] [14 15]] -> 1 to 3 columns
print(arr[: , ::2]) # [[ 1  3] [ 5  7] [ 9 11] [13 15]] -> 0 to end column with 2 step
print(arr[: , ::-1]) # [[ 4  3  2  1] [ 8  7  6  5] [12 11 10  9] [16 15 14 13]] -> reverse columns
print(arr[: , ::-2]) # [[ 4  2] [ 8  6] [12 10] [16 14]] -> reverse with 2 step

# row & column
print(arr[1:3 , 1:3]) #[[ 6  7] [10 11]] -> 1 to 3 row , 1 to 3 column
print(arr[2:: , 2::]) # [[11 12] [15 16]] -> row 2 to  end , cols 2 to end