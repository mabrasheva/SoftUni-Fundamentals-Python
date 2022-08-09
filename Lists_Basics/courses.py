# On the first line, you will receive a single number n.
# On the following n lines, you will receive names of courses.
# You should create a list of courses and print it.

courses_count = int(input())
courses_list = list()

for number in range(courses_count):
    courses_list.append(input())

print(courses_list)
