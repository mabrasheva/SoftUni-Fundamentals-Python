# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

message = input().split()
secret_message = []

for word in message:
    secret_word = []
    first_letter = ""
    rest_letters = ""
    for character in word:
        if character.isdigit():
            first_letter += character
        else:
            rest_letters += character
    first_letter = chr(int(first_letter))
    rest_letters = list(rest_letters)
    rest_letters[0], rest_letters[-1] = rest_letters[-1], rest_letters[0]
    rest_letters = "".join(rest_letters)
    secret_word = first_letter + rest_letters

    secret_message.append(secret_word)

print(*secret_message)
