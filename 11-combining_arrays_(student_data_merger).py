import numpy as np

# Each row represents one student.
# Column 0 represents the student's ID.
# Column 1 represents the student's grade.

group_a = np.array([[101, 85],
                    [102, 90]])

group_b = np.array([[103, 78],
                    [104, 95]])
print("group a:\n ",group_a)
print("group b:\n ",group_b)
print("Print the shape of both arrays: ")
print(f"group_a shape:{group_a.shape}")
print(f"group_b shape:{group_b.shape}\n")

print("combine both groups vertically into one array")
print("1- Use np.concatenate()")
concat_arr = np.concatenate((group_a, group_b), axis=0)
print(concat_arr)

print("2- Use np.vstack()")
vstack_arr = np.vstack((group_a, group_b))
print(vstack_arr)

print("Verify that the results are identical:")
print(np.array_equal(concat_arr, vstack_arr))


print("\nCreate an array containing the ages of the students in group_a")
ages = np.array([19, 20])
ages=ages.reshape(-1,1)
# Note: The -1 lets NumPy automatically calculate the number of rows, while 1 specifies one column.
print("ages in group_a: \n",ages)

print("Append the ages as a new column beside the existing student data:")
print("1- Use np.concatenate()")
concat_arr_2=np.concatenate((group_a,ages),axis=1)
print(concat_arr_2)

print("2- Use np.hstack()")
hstack_arr = np.hstack((group_a,ages))
print(hstack_arr)
# Final array columns: Student ID, Grade, Age.

print(f"Shape of arr after adding ages column: {hstack_arr.shape}")

print("Verify that the results are identical:")
print(np.array_equal(concat_arr_2, hstack_arr))


