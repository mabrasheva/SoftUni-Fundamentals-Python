# Write a password reset program that performs a series of commands upon a predefined string.
# First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with
# commands split by a single space. The commands will be the following:
# •	"TakeOdd"
# o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
# •	"Cut {index} {length}"
# o	Gets the substring with the given length starting from the given index from the password and removes its first
# occurrence, then prints the password on the console.
# o	The given index and the length will always be valid.
# •	"Substitute {substring} {substitute}"
# o	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and
# prints the result.
# o	If it doesn't, prints "Nothing to replace!".
# Input
# •	You will be receiving strings until the "Done" command is given.
# Output
# •	After the "Done" command is received, print:
# o	"Your password is: {password}"
# Constraints
# •	The indexes from the "Cut {index} {length}" command will always be valid.

def take_odd(new_password):
    new_password = [char for index, char in enumerate(new_password) if index % 2 != 0]
    new_password = "".join(new_password)
    print(new_password)
    return new_password


def cut(command, new_password):
    command = command.split()
    index, length = int(command[1]), int(command[2])
    substring = new_password[index:index + length]
    new_password = new_password.replace(substring, "", 1)
    print(new_password)
    return new_password


def substitute(command, new_password):
    command = command.split()
    substring, substitute = command[1], command[2]
    if substring in new_password:
        new_password = new_password.replace(substring, substitute)
        print(new_password)
    else:
        print("Nothing to replace!")
    return new_password


predefined_string = input()
new_password = predefined_string
command = input()
while command != "Done":
    if command.startswith("TakeOdd"):
        new_password = take_odd(new_password)
    elif command.startswith("Cut"):
        new_password = cut(command, new_password)
    elif command.startswith("Substitute"):
        new_password = substitute(command, new_password)

    command = input()

print(f"Your password is: {new_password}")
