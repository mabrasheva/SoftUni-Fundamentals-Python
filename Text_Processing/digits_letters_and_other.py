# Write a program that receives a single string. On the first line, print all the digits found in the string, on the
# second – all the letters, and on the third – all the other characters. There will always be at least one digit, one
# letter, and one other character.

def all_digits(word: str):
    word = [letter for letter in word if letter.isdigit()]
    return word


def all_letters(word: str):
    word = [letter for letter in word if letter.isalpha()]
    return word


def all_other_characters(word: str):
    word = [letter for letter in word if not letter.isalnum()]
    return word


string = input()
digits = all_digits(string)
letters = all_letters(string)
others = all_other_characters(string)

print(*digits, sep="")
print(*letters, sep="")
print(*others, sep="")
