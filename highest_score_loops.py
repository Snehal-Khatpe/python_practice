"""
write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

"""



# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

max_value = student_scores[0]
for score in student_scores:
  if score > max_value:
    max_value = score

print(f"The highest score in the class is: {max_value}")
