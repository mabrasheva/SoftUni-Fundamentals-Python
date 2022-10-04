# Write a program that receives a list of characters separated by ", ". It should create a dictionary with each
# character as a key and its ASCII value as a value. Try solving that problem using comprehension.

# Version 1:
#
# characters_list = input().split(", ")
# result = {}
#
# for character in characters_list:
#     result[character] = ord(character)
#
# print(result)

# Version 2:

result = {character: ord(character) for character in input().split(", ")}
print(result)
