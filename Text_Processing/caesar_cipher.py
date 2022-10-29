# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character with
# the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

# Solution 1:

# unencrypted_string = input()
# encrypted_string = ""
# for character in unencrypted_string:
#     encrypted_string += chr(ord(character) + 3)
# print(encrypted_string)

# Solution 2 with comprehension:

encrypted_string = ('').join([chr(ord(character) + 3) for character in input()])
print(encrypted_string)
