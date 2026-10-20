import numpy as np

student_ids = np.array([101, 102, 103, 104, 105])
grades = np.array([78, 95, 85, 95, 60])

print(f"Student IDs: {student_ids}")
print(f"Grades: {grades}")

# np.sort(): Returns a sorted copy of the array without modifying the original array.
print("\n\n1. Sort the grades in ascending order:")
sorted_grades=np.sort(grades)
print(sorted_grades)

# np.argsort(): Returns the indices that would sort the array in ascending order.
print("\n2. Find the indices that would sort the grades in ascending order:")
sorting_order= np.argsort(grades)
print(sorting_order)

# np.where(): Returns a tuple containing arrays of indices that satisfy the given condition.
print("\n3. Find the indices of students who scored 95:")
score_95=np.where(grades==95)
print(score_95[0])
print("student IDs of students who scored 95:")
print(student_ids[score_95])

print("\n4. Find the indices of the highest and lowest grades:")
# np.argmax(): Returns the index of the maximum element in the array.
highest_grade_index=np.argmax(grades)
print("Highest Grade Index:",highest_grade_index)
# np.argmin(): Returns the index of the minimum element in the array.
lowest_grade_index=np.argmin(grades)
print("Lowest Grade Index: ",lowest_grade_index)

print("\n5. Identify the student IDs with the highest and lowest grades:")
highest_student_id =student_ids[highest_grade_index]
print(f"Highest student ID: {highest_student_id}, Grade: {grades[highest_grade_index]}")
lowest_student_id =student_ids[lowest_grade_index]
print(f"Lowest student ID: {lowest_student_id} , Grade: {grades[lowest_grade_index]}")
