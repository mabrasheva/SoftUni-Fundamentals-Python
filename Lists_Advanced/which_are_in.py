# You will be given two sequences of strings, separated by ", ".
# Print a new list containing only the strings from the first input line, which are substrings of any string in the
# second input line.

first_string = input().split(", ")
second_string = input()
final_list = [element for element in first_string if element in second_string]

print(final_list)
