import numpy as np

student_ids = np.array([101, 102, 103, 104, 105])
grades = np.array([78, 85, 62, 90, 55])

print("Original Student Data:")
print("Student IDs:", student_ids)
print("Grades:", grades)


# np.append(): Returns a new array with the specified values added to the end.
student_ids = np.append(student_ids, 106)
grades = np.append(grades, 88)

print("\n1. Add a new student:")
print("Updated Student IDs:", student_ids)
print("Updated Grades:", grades)


# np.delete(): Returns a new array with the elements at the specified indices removed.
student_ids = np.delete(student_ids, 2)
grades = np.delete(grades, 2)

print("\n2. Remove a student:")
print("Updated Student IDs:", student_ids)
print("Updated Grades:", grades)


# Boolean indexing: Selects or modifies elements based on a condition.
grades[student_ids == 102] = 95

print("\n3. Correct a student's grade:")
print("Student IDs:", student_ids)
print("Updated Grades:", grades)


# np.clip(): Returns an array with values limited to the specified minimum and maximum.
grades = np.clip(grades, 0, 100)

print("\n4. Limit grades to the range (0-100):")
print("Updated Grades:", grades)


print("\n5. Final Student Data:")
print("Student IDs:", student_ids)
print("Grades:", grades)

