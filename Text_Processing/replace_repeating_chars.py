# Write a program that reads a string from the console and replaces any sequence of the same letters with a single
# corresponding letter.

input_string = input()
result = ""

for index, letter in enumerate(input_string):
    if index == 0:
        result = letter
    else:
        if letter != result[-1]:
            result += letter
print(result)
