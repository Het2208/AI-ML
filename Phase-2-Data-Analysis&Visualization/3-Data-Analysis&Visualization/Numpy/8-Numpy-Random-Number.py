import numpy as np

# Integers
rng = np.random.default_rng()

# second is exclusive
print(rng.integers(1,7))

# 4 Digit OTP
print(rng.integers(1000,10000))

print(rng.integers(low = 1,high = 100 , size=3))  # 1 row , 3 column
print(rng.integers(low = 1,high = 100 , size=(3,2))) # 3 row , 2 column

print("*" * 50)

# Floating point
print(np.random.uniform(low = -1 , high=1))

print(np.random.uniform(low = -1 , high=1 , size=3))

print(np.random.uniform(low = -1 , high=1 , size=(3,2)))

print("*" * 50)
# shuffle method
arr = np.array([-3, 5, -1, 8, 0, -7, 2])

rng = np.random.default_rng()
rng.shuffle(arr)
print(arr)

print("*" * 50)
# choice method
fruits = np.array(["apple" , "orange" , "peach" , "grape" , "banana"])

fruit = rng.choice(fruits)
print(fruit)

fruits = rng.choice(fruits , size=(2,3))
print(fruits)

fruits = rng.choice(fruits , size=2)
print(fruits)



