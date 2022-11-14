# On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
# •	"InsertSpace:|:{index}":
# o	Inserts a single space at the given index. The given index will always be valid.
# •	"Reverse:|:{substring}":
# o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
# o	If not, print "error".
# o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
# •	"ChangeAll:|:{substring}:|:{replacement}":
# o	Changes all occurrences of the given substring with the replacement text.
# Input / Constraints
# •	On the first line, you will receive a string with a message.
# •	On the following lines, you will be receiving commands, split by ":|:".
# Output
# •	After each set of instructions, print the resulting string.
# •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"

def insert_space(command: list, message: str):
    index = int(command[1])
    message = message[:index] + " " + message[index:]
    print(message)
    return message


def reverse(command: list, message: str):
    substring = command[1]
    if substring in message:
        reverse_substring = substring[::-1]
        message = message.replace(substring, "", 1)
        message = message + reverse_substring
        print(message)
    else:
        print("error")
    return message


def change_all(command: list, message: str):
    substring, replacement = command[1], command[2]
    message = message.replace(substring, replacement)
    print(message)
    return message


concealed_message = input()
new_message = concealed_message
command = input()
while command != "Reveal":
    command = command.split(":|:")
    action = command[0]
    if action == "InsertSpace":
        new_message = insert_space(command, new_message)
    elif action == "Reverse":
        new_message = reverse(command, new_message)
    elif action == "ChangeAll":
        new_message = change_all(command, new_message)
    command = input()

print(f"You have a new text message: {new_message}")
