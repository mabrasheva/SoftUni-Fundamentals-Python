# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input, you will receive the encrypted message.
# After that, until the "Decode" command is given, you will be receiving strings with instructions for different
# operations that need to be performed upon the concealed message to interpret it and reveal its true content.
# There are several types of instructions, split by '|'
# •	"Move {number of letters}":
# o	Moves the first n letters to the back of the string
# •	"Insert {index} {value}":
# o	Inserts the given value before the given index in the string
# •	"ChangeAll {substring} {replacement}":
# o	Changes all occurrences of the given substring with the replacement text
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by '|' .
# Output
# •	After the "Decode" command is received, print this message:
# "The decrypted message is: {message}"

def move(command: list, encrypted: str):
    number_of_letters = int(command[1])
    encrypted = encrypted[number_of_letters:] + encrypted[:number_of_letters]
    return encrypted


def insert(command: list, encrypted: str):
    index, value = int(command[1]), command[2]
    encrypted = encrypted[:index] + value + encrypted[index:]
    return encrypted


def change_all(command: list, encrypted: str):
    substring, replacement = command[1], command[2]
    encrypted = encrypted.replace(substring, replacement)
    return encrypted


message = input()
decrypted = ""
instruction = input()
while instruction != "Decode":
    instruction = instruction.split("|")
    action = instruction[0]
    if action == "Move":
        message = move(instruction, message)
    elif action == "Insert":
        message = insert(instruction, message)
    elif action == "ChangeAll":
        message = change_all(instruction, message)

    instruction = input()

print(f"The decrypted message is: {message}")
