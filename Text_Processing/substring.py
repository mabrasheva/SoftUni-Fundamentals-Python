# On the first line, you will receive a string. On the second line, you will receive a second string. Write a program
# that removes all the occurrences of the first string in the second until there is no match. At the end, print the
# remaining string.

first = input()
second = input()

while first in second:
    second = second.replace(first, "")

print(second)
