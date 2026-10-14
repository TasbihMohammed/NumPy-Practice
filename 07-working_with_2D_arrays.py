import numpy as np

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix)

print("Matrix's shape:" , matrix.shape)

print("Number of dimensions:", matrix.ndim)

print("First row: " , matrix[0,:])

print("Last column: " , matrix[:,-1])

print("Access the element 50 using indexing: " , matrix[1,1])

print("Sum of all elements: ",matrix.sum())

print("Average of all elements: ",matrix.mean())

print("Extract the first two rows and the last two columns: ")
new_matrix= matrix[0:2 , -2:]
print(new_matrix)



