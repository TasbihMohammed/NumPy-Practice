import numpy as np
numbers=np.array([12,45,67,23,89,34,90,56,10,78])

print(numbers)

print("All numbers greater than 50: ")
greater_than_50 = numbers[numbers>50]
print(greater_than_50)

print("All numbers less than or equal to 30: ")
less_or_equal_30 = numbers[numbers<=30]
print(less_or_equal_30)

print("All even numbers: ")
even_numbers= numbers[numbers%2==0]
print(even_numbers)

print("Number of numbers greater than 60:")
N_greater_than_60 = sum(numbers>60)
print(N_greater_than_60)

print("New array containing only numbers between 20 and 70, inclusive:")
new_arr=numbers[(numbers>=20) & (numbers<=70)]
print(new_arr)
