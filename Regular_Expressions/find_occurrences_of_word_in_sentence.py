# Write a program that finds how many times a word is used in a string.
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.

import re

string = input()
word = input()

pattern = rf"\b{word}\b"

matches = re.findall(pattern, string, flags=re.IGNORECASE)
print(len(matches))
