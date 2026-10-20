import numpy as np

arr= np.arange(1,13)

print("Reshape the array into a 3 × 4 matrix: ")
new_arr=arr.reshape(3,4)
print(new_arr)
print("Shape: ",new_arr.shape)

print("Reshape the array into a 4 × 3 matrix: ")
new_arr2=arr.reshape(4,3)
print(new_arr2)
print("Shape: ",new_arr2.shape)

print("Flatten the 3 × 4 matrix into a 1D array :")
print(new_arr.flatten())

#Try to reshape the array containing 12 elements into a 5 × 3 matrix
#What happens when you run the code?
#Why does NumPy raise an error?
#Answer:

#Reshaping the array into a 5 × 3 matrix raises a `ValueError`
# because the original array contains 12 elements,
# while the new matrix requires 15 elements.
# The total number of elements must remain the same when using `reshape()`.





