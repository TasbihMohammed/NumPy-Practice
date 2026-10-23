import numpy as np

# Create a 2D array representing the scores of 3 students in 4 subjects.
scores = np.array([
    [85, 90, 78, 92],
    [70, 88, 95, 80],
    [90, 76, 84, 89]
])

print("Original Scores:")
print(scores)
print("\nOriginal Shape:", scores.shape)
print("Original Dimensions:", scores.ndim)

# Transpose the array by swapping rows and columns.
transposed_arr = np.transpose(scores)

print("\n1. Transpose Using np.transpose():")
print(transposed_arr)
print("Shape:", transposed_arr.shape)


# Use .T as a shorthand for transposing a 2D array.
transposed_arr2 = scores.T

print("\n2. Transpose Using .T:")
print(transposed_arr2)

# Check whether both transposed arrays are identical.
print("Are Both Arrays Identical?",
      np.array_equal(transposed_arr, transposed_arr2))

# Use np.swapaxes() to swap axis 0 (rows) with axis 1 (columns).
swapped_arr = np.swapaxes(scores, 0, 1)

print("\n3. Swap Axes Using np.swapaxes():")
print(swapped_arr)
print("Shape After Swapping:", swapped_arr.shape)


# Use np.expand_dims() to add a new dimension at axis 0.
# The array shape changes from (3, 4) to (1, 3, 4).
expanded_arr = np.expand_dims(scores, axis=0)

print("\n4. Expand Dimensions Using np.expand_dims():")
print(expanded_arr)
print("Shape After Expansion:", expanded_arr.shape)
print("Dimensions After Expansion:", expanded_arr.ndim)

# Use np.squeeze() to remove dimensions of size 1.
# The array shape changes from (1, 3, 4) back to (3, 4).
squeezed_arr = np.squeeze(expanded_arr)

print("\n5. Remove Extra Dimensions Using np.squeeze():")
print(squeezed_arr)
print("Shape After Squeezing:", squeezed_arr.shape)
print("Dimensions After Squeezing:", squeezed_arr.ndim)
