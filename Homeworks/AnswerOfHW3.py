#Answer of homework 3
students_names = [*range(5)]
student_grades = [*range(5)]

for i in range(2):
  print("enter " ,i+1," .th student name")
  students_names[i] = input()

print(students_names)

for j in range(len(students_names)):
  print("write", students_names[j], "'s midterm grade")
  midterm = int(input()) * 0.3
  print("write", students_names[j], "'s project grade")
  project = int(input()) * 0.3
  print("write", students_names[j], "'s final grade")
  final = int(input()) * 0.4
  passing_grade = midterm + project + final 
  d[j] = passing_grade
  student_grades[j] = passing_grade

print(student_grades)

res = {students_names[i]: student_grades[i] for i in range(len(students_names))}
print(res)
#highest grade set in first value, and lowest grade seti last value
res_n = {k : v for k, v in sorted(res.items(), key=lambda item : item[1], reverse=True)}
print(res_n)