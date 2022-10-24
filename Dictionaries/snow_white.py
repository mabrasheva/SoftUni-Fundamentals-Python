# Snow White loves her dwarfs, but there are so many, and she doesn't know how to order them. Does she order them by
# name? Or by color of their hat? Or by physics? She can't decide, so it's up to you to write a program that does it for
# her.
# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# •	If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should store
# them both.
# •	If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in descending
# order and then by total count of dwarfs with the same hat color in descending order.
# Then you must print them all.
# Input
# •	The input will consist of several input lines, containing dwarf data in the format, specified above.
# •	The input ends when you receive the command "Once upon a time".
# Output
# •	As output, you must print the dwarfs, ordered in the way, specified above.
# •	The output format is: "({hat_color}) {name} <-> {physics}"
# Constraints
# •	The "dwarf_name" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# •	The "dwarf_hat_color" will be a string which may contain any ASCII character except ' ' (space), '<', ':', '>'.
# •	The "dwarf_physics" will be an integer in range [0, 231 – 1].
# •	There will be no invalid input lines.
# •	If all sorting criteria fail, the order should be by order of input.
# •	Allowed working time / memory: 100ms / 16MB.

def order_dwarfs(input_name: str, input_color: str, input_physics: int):
    if input_color not in dwarfs:
        dwarfs[input_color] = {input_name: input_physics}
    else:
        if input_name not in dwarfs[input_color]:
            dwarfs[input_color].update({input_name: input_physics})
        else:
            if input_physics > dwarfs[input_color][input_name]:
                dwarfs[input_color][input_name] = input_physics


dwarfs = {}
command = input()
while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    physics = int(physics)
    order_dwarfs(name, color, physics)

    command = input()

dwarfs_list = []
for hat_color, dwarf in dwarfs.items():
    for dwarf_name, dwarf_physics in dwarf.items():
        dwarfs_list.append(
            {"len": len(dwarf), "hat_color": hat_color, "dwarf_name": dwarf_name, "dwarf_physics": dwarf_physics})
        # print(*dwarfs_list, sep ="\n")
for line in sorted(dwarfs_list, key=lambda item: (item['dwarf_physics'], item['len']), reverse=True):
    print(f"({line['hat_color']}) {line['dwarf_name']} <-> {line['dwarf_physics']}")
