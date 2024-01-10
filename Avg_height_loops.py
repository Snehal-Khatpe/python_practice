""" 
write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
There are a total of 7 heights in student_heights
1146 ÷ 7 = 163.71428571428572
Average height rounded to the nearest whole number = 164
Important You should not use the sum() or len() functions in your answer. 
"""



# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
total_student =0

for height in student_heights:
    total_height+=height
    total_student+=1

average_height = round(total_height/total_student)
print(f"total height {total_height}")
print(f"number of students {total_student}")
print(f"average height {average_height}")
