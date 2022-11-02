# Write a program that receives strings on different lines and extracts only the numbers.
# Print all extracted numbers on a single line, separated by a single space.

import re

pattern = r'\d+'

result = []

line = input()
while line:
    matches = re.findall(pattern, line)
    if matches:
        result += matches

    line = input()

print(*result)
