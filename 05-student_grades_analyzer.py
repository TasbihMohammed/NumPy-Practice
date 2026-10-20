import numpy as np

def student_grades_analyzer(grades):
    print("Average Grade: ",grades.mean())
    print("Highest Grade: ",grades.max())
    print("Lowest Grade: ",grades.min())
    print("Students who scored 80 or higher: ")
    print(np.sum(grades>=80))
    print("Passing grades (50 or higher): ")
    print(grades[grades>=50])
    print("Grades sorted in ascending order: ")
    sorted_grades=np.sort(grades)
    print(sorted_grades)


def convert_string_to_array(input_string,dtype=float):
    converted_values= map(dtype,input_string.split(","))
    numpy_array= np.array(list(converted_values))

    return numpy_array


print("Student Grades Analyzer".center(40,"*"))
grades_input=input("Enter student grades separated by commas: ")
grades=convert_string_to_array(grades_input)

student_grades_analyzer(grades)