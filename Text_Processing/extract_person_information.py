# Write a program that reads N lines of strings and extracts the name and the age of a given person:
# •	The person's name will be surrounded by "@" and "|" in the format "@{name}|".
# •	The person's age will be surrounded by "#" and "*" in the format "#{age}*".
# Example: "Hello my name is @Peter| and I am #20* years old."
# For each found name-age pair, print a line in the following format "{name} is {age} years old."

count = int(input())

for line in range(count):
    person = input()
    name = ""
    age = ""
    name_start_index = name_end_index = age_start_index = age_end_index = 0
    for index, character in enumerate(person):
        if character == "@":
            name_start_index = index + 1
        if character == "|":
            name_end_index = index - 1

        if character == "#":
            age_start_index = index + 1
        if character == "*":
            age_end_index = index - 1

    name = person[name_start_index:name_end_index + 1]
    age = person[age_start_index:age_end_index + 1]
    print(f"{name} is {age} years old.")
