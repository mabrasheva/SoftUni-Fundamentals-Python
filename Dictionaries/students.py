# You will be receiving names of students, their ID, and a course of programming they have taken in the format
# "{name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format:
# "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique

student = input()
students_dict = {}
while ":" in student:
    name, student_id, student_course = student.split(":")
    students_dict[name] = student_id, student_course

    student = input()

course = student.replace("_", " ")

for key, value in students_dict.items():
    student_id = value[0]
    student_course = value[1]
    if student_course == course:
        print(f'{key} - {student_id}')
