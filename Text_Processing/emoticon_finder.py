# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

input_text = input()

for index, character in enumerate(input_text):
    if character == ":":
        print(character + input_text[index + 1])
