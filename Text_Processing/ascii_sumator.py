# Write a program that prints the sum of all found characters between two given characters (their ASCII code).
# On each of the first two lines, you will receive a single character. On the last line, you get a random string.
# Print the sum of the ASCII values of all characters in the random string between the two given characters in the ASCII
# table.

first_character = input()
second_character = input()
input_string = input()
total_sum = 0

for character in input_string:
    if ord(first_character) < ord(character) < ord(second_character):
        total_sum += ord(character)

print(total_sum)
