# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

def characters_between(start, end):
    list_characters = []
    for character in range(ord(start) + 1, ord(end)):
        list_characters.append(chr(character))
    return list_characters


start_character = input()
end_character = input()

result = characters_between(start_character, end_character)

print(*result)
