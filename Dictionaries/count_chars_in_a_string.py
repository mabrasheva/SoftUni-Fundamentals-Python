# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

input_string = input()
characters_dict = {}
for character in input_string:
    if not character.isspace():
        if character not in characters_dict:
            characters_dict[character] = 0
        characters_dict[character] += 1

for key, value in characters_dict.items():
    print(f"{key} -> {value}")
