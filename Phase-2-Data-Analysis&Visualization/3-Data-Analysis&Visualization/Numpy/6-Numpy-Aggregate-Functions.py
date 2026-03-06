#Aggregate function -> Summarize data and return a single value

import numpy as np

arr = np.array([[1,2,3,4,5] ,
                [6,7,8,9,10]])

print(np.sum(arr)) # 55
print(np.max(arr)) # 10
print(np.min(arr)) # 1
print(np.argmax(arr)) # 9 (Index of max element)
print(np.argmin(arr)) # 0 (Index of min element)
print(np.mean(arr)) # 5.5 (Average)
print(np.median(arr)) # 5.5 (Medain of data)
print(np.std(arr)) # 2.8722813232690143 (Standard Deviation)
print(np.var(arr)) # 8.25 (Variance)

print("*" * 50)

print(np.sum(arr , axis=0)) # [ 7  9 11 13 15] -> sum colums wise
print(np.sum(arr , axis=1)) # [ 15 , 40] -> sum row wise

print("*" * 50)

print(np.count_nonzero(arr)) # 10 (Count non zero element)
print(np.prod(arr)) # 3628800 (Product of all element)
print(np.cumsum(arr)) # [ 1  3  6 10 15 21 28 36 45 55] (Cumulative Sum)
print(np.cumprod(arr)) #[ 1  2  6  24  120  720  5040  40320  362880  3628800] (Cumulative Product)
print(np.ptp(arr)) # 9 (max - min (Peak-to-Peak))
print(np.any(arr > 50))  # False -> True if any value > 5
print(np.all(arr > 0))  # True -> True if all positive


print("*" * 50)

# A percentile tells you the value below which a given % of data falls.
# 25th percentile (Q1) → 25% data below this value
# 50th percentile (Q2 / Median) → middle value
# 75th percentile (Q3) → 75% data below this value
print(np.percentile(arr, 25))  # 3.25
print(np.percentile(arr, 50))  # 5.5
print(np.percentile(arr, 75))  # 7.75
