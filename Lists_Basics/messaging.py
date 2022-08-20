# On the first line, you will receive a sequence of numbers separated by a single space.
# On the second line, you will receive a string.
# Your task is to write a program that sends a message only using chars from the given string.
# Each char the program adds to the message should be found by its index.
# The index you are looking for is the sum of a number's digits from the sequence.
# If the index is greater than the length of the text, continue counting from the beginning (so that you always have a
# valid index). When you find a char, you should add it to the message and remove it from the string.
# It means that for the following index, the text will be with one character less.
# Print the final message.

list_numbers = input().split()
initial_string = list(input())
index_list = []
message = ""

for number in list_numbers:
    index = 0
    for digit in number:
        index += int(digit)
    index_list.append(index)

for index in index_list:
    if index >= len(initial_string):
        index -= len(initial_string)
    message += initial_string[index]
    initial_string.remove(initial_string[index])

print(message)
