# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N times,
# where N is the length of the string. Print the final strings concatenated into one string.

sequence = input().split()
result = ""
for word in sequence:
    result += word * len(word)

print(result)
