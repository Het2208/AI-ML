import numpy as np

print("*" * 50)

# Scaler arithmetic (single value)
arr = np.array([1,2,3])
print(arr + 2) # [3 4 5]
print(arr - 2) # [-1  0  1]
print(arr * 2) # [2 4 6]
print(arr // 2) # [0 1 1]
print(arr ** 2) # [1 4 9]

print("*" * 50)

# Vectorized math functions
arr = np.array([1.2,2.6,3.5])
print(np.ceil(arr)) # [2. 3. 4.]
print(np.floor(arr)) # [1. 2. 3.]
print(np.round(arr)) # [1. 3. 4.]
print(np.sqrt(arr)) # [1.09544512 1.61245155 1.87082869]
print(np.pi) # 3.141592653589793

print("*" * 50)

# Exercise 1
redii = np.array([1,2,3])
print(2 * np.pi* redii) # 2 * pi * r -> [ 6.28318531 12.56637061 18.84955592]
print(np.pi * redii**2) # pi * r * r -> [ 3.14159265 12.56637061 28.27433388]

print("*" * 50)

# Exercise 2 (Element-wise arithmetic)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(arr1 + arr2) # [5 7 9]
print(arr1 - arr2) # [-3 -3 -3]
print(arr1 * arr2) # [ 4 10 18]
print(arr1 // arr2) # [0 0 0]
print(arr1 ** arr2) # [  1  32 729]

print("*" * 50)

# Comparison operators
scores = np.array([48,100,67,94,22])
print(scores == 100) # [False  True False False False]
print(scores > 35) # [ True  True  True  True False]
print(scores <= 35) # [False False False False  True]

scores[scores < 35] = 0
print(scores) # [ 48 100  67  94   0]