# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows.
# On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to
# 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.

students_count = int(input())
students = {}

for student in range(students_count):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []
    students[name].append(grade)

# for student, grades in list(students.items()):
#     average_grade = sum(grades) / len(grades)
#     if average_grade >= 4.50:
#         students[student] = average_grade
#     else:
#         del students[student]

top_students = {}
for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        top_students[student] = average_grade

for student, average_grade in top_students.items():
    print(f"{student} -> {average_grade:.2f}")
