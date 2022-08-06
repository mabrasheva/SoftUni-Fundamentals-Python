# Write a program that prints part of the ASCII table characters on the console, separated by a single space.
# On the first line of input, you will receive the char index you should start with.
# On the second line - the index of the last character you should print.

start = int(input())
end = int(input())
for character in range(start, end + 1):
    print(chr(character), end=" ")
