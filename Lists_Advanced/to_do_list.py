# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint
# •	Use the pop() and insert() methods.

command = input()

tasks_list = []
result = []

while command != "End":
    command = command.split("-")

    notes_list = [note_importance, note_data] = [int(command[0]), command[1]]
    tasks_list.append(notes_list)

    result = [data[1] for data in sorted(tasks_list)]

    command = input()

print(result)
