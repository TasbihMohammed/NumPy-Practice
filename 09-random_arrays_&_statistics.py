import numpy as np

print("Create a NumPy array containing 20 random integers between 1 and 100: ")
arr=np.random.randint(1,101,size=20)
print(arr)
print(f"Size: {arr.size}, Shape: {arr.shape}, N of dimintions: {arr.ndim}")

print("*"*50)

print("Statistics: ")
print("The mean (average) of the numbers: ",arr.mean())
print("The median of the numbers: ",np.median(arr))
print("The standard deviation: ",arr.std())
print("The minimum value: ",arr.min())
print("The maximum value: ",arr.max())
print("The sum of all elements: ",arr.sum())

print("*"*50)

print("Sorting and Filtering: ")
print("Sort the array in ascending order:")
sorted_arr_ascendingly=np.sort(arr)
print(sorted_arr_ascendingly)
print("Sort the array in Descending order:")
sorted_arr_descendingly=(np.sort(arr)[::-1])
print(sorted_arr_descendingly)
print("Create a new array containing only numbers greater than the mean: ")
new_arr=arr[arr>arr.mean()]
print(new_arr)
print("Count how many numbers are greater than the mean: ")
greater_than_the_mean_counter= np.sum(arr>arr.mean())

print("*"*50)

print("Challenge: ")
print("Create a NumPy array containing 20 random integers between 1 and 100: ")
array=np.random.randint(1,101,size=20)

print("Reshape the array into a 4 × 5 matrix: ")
matrix= array.reshape(4,5)
print(matrix)

print("Calculate and print the mean of each row separately: ")
row_means=matrix.mean(axis=1)
print(row_means)







