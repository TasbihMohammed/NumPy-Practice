import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])
print(numbers)

print("Print the first element.")
print(numbers[0])

print("Print the last element.")
print(numbers[-1])

print("Print the elements from 20 to 40 using slicing.")
print(numbers[1:4])

print("Print the last three elements.")
print(numbers[-3:])

print("Print the elements at even indexes: 0, 2, and 4.")
#Using Indexing:
print(numbers[::2])



