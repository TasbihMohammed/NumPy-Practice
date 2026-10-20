import numpy as np
#create array(numpu arrays are stored in one continuous place in memory):
arr=np.array([80, 95, 72, 88, 100])
print(arr)
#number of elements in array:
print(arr.size)
#array shape:
print(arr.shape)
#number of dimentions:
print(arr.ndim)

arr2=np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr2)
print(arr2.size)
print(arr2.shape)
print(arr2.ndim)
