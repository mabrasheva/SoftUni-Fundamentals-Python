# Input
# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this
# command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
# Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of
# the list. Otherwise, skip this command.
# Constraints
# •	There won't be any duplicate items in the initial list
# Output
# •	Print the list with all the groceries, joined by ", ":
# "{firstGrocery}, {secondGrocery}, … {nthGrocery}"

initial_list = input().split("!")


def urgent(item):
    if item not in initial_list:
        initial_list.insert(0, item)


def unnecessary(item):
    if item in initial_list:
        initial_list.remove(item)


def correct(old_item, new_item):
    for item in range(len(initial_list)):
        if old_item == initial_list[item]:
            initial_list[item] = new_item


def rearrange(item):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)


command = input()
while command != "Go Shopping!":
    command = command.split()

    if command[0] == "Urgent":
        urgent(command[1])

    elif command[0] == "Unnecessary":
        unnecessary(command[1])

    elif command[0] == "Correct":
        correct(command[1], command[2])

    elif command[0] == "Rearrange":
        rearrange(command[1])

    command = input()

print(", ".join(initial_list))
