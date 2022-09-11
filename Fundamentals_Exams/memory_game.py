# Write a program that recreates the Memory game.
# On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the
# player receives "end" from the console, you will receive strings with two integers separated by a space, representing
# the indexes of elements in the sequence.
# If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you
# should add two matching elements at the middle of the sequence in the following format:
# "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
# Input
# •	On the first line, you will receive a sequence of elements
# •	On the following lines, you will receive integers until the command "end"
# Output
# •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console
# the following message:
# "Congrats! You have found matching elements - ${element}!"
# •	If the player hit two different elements, you should print on the console the following message:
# "Try again!"
# •	If the player hit all matching elements before he receives "end" from the console, you should print on the console
# the following message:
# "You have won in {number of moves until now} turns!"
# •	If the player receives "end" before he hits all matching elements, you should print on the console the following
# message:
# "Sorry you lose :(
# {the current sequence's state}"
# Constraints
# •	All elements in the sequence will always have a matching element.

elements = input().split()
moves = 0
win = False

while True:

    if len(elements) == 0:
        win = True
        break

    command = input()
    if command == "end":
        break
    command = command.split()
    command = list(map(int, command))
    command = sorted(command, reverse=True)
    moves += 1

    first_index = command[0]
    second_index = command[1]

    # If two equal indexes or indexes out of bounds of the sequence add two matching elements at the middle of the
    # sequence:
    if first_index == second_index or \
            first_index >= len(elements) or second_index >= len(elements) or \
            first_index < 0 or second_index < 0:
        middle_of_elements_list = len(elements) // 2
        elements.insert(middle_of_elements_list, f"-{moves}a")
        elements.insert(middle_of_elements_list + 1, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[first_index] == elements[second_index]:
        deleted_element = elements[first_index]
        del elements[first_index]
        del elements[second_index]
        print(f"Congrats! You have found matching elements - {deleted_element}!")

    elif elements[first_index] != elements[second_index]:
        print("Try again!")

if win:
    print(f"You have won in {moves} turns!")
else:
    print("Sorry you lose :(")
    print(*elements, sep=" ")
