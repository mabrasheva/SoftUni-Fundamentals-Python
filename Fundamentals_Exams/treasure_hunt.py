# Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
# •	"Loot {item1} {item2}…{itemn}":
# o	Pick up treasure loot along the way. Insert the items at the beginning of the chest.
# o	If an item is already contained, don't insert it.
# •	"Drop {index}":
# o	Remove the loot at the given position and add it at the end of the treasure chest.
# o	If the index is invalid, skip the command.
# •	"Steal {count}":
# o	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there
# are.
# o	Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of
# all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."
# Input
# •	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
# •	On the following lines, until "Yohoho!", you will be receiving commands.
# Output
# •	Print the output in the format described above.
# Constraints
# •	The loot items will be strings containing any ASCII code.
# •	The indexes will be integers in the range [-200…200]
# •	The count will be an integer in the range [1….100]

def loot(items_to_add, items_existing_list):
    for item in items_to_add:
        if item not in items_existing_list:
            items_existing_list.insert(0, item)
    return items_existing_list


def drop(index, items_existing_list):
    if 0 <= index < len(items_existing_list):
        items_existing_list.append(items_existing_list[index])
        del items_existing_list[index]
    return items_existing_list


def steal(count, items_existing_list):
    if count > len(items_existing_list):
        count = len(items_existing_list)
    stolen = []
    for item in range(len(items_existing_list) - count, len(items_existing_list)):
        stolen.append(items_existing_list[item])
    print(", ".join(stolen))
    items_existing_list = items_existing_list[:len(items_existing_list) - count]
    return items_existing_list


items = input().split("|")

command = input()
while command != "Yohoho!":
    command = command.split()
    if command[0] == "Loot":
        items_list = command[1::]
        items = loot(items_list, items)
    elif command[0] == "Drop":
        index_drop = int(command[1])
        items = drop(index_drop, items)
    elif command[0] == "Steal":
        count_steal = int(command[1])
        items = steal(count_steal, items)

    command = input()

if len(items) > 0:
    total_sum = 0
    for item in items:
        total_sum += len(item)
    average_sum = total_sum / len(items)
    print(f"Average treasure gain: {average_sum:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
