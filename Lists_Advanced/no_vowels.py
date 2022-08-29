# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
# Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

vowels = ['a', 'o', 'u', 'e', 'i']
input_text = input()

result = [character for character in input_text if character.lower() not in vowels]
print("".join(result))
