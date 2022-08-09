# On the first line, you will receive a number n.
# On the second line, you will receive a word.
# On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

strings_count = int(input())
word = input()
strings_list = list()
strings_filtered_list = list()

# Version 1:

# for string in range(strings_count):
#     current_string = input()
#     strings_list.append(current_string)
#     if word in current_string:
#         strings_filtered_list.append(current_string)

# Version 2:

for line in range(strings_count):
    current_string = input()
    strings_list.append(current_string)

for string in strings_list:
    if word in string:
        strings_filtered_list.append(string)

print(strings_list)
print(strings_filtered_list)
