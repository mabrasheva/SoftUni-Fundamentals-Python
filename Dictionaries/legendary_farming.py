# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that
# the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
#
# Input
# •	Each line comes in the following format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Output
# •	On the first line, print the obtained item in the format: "{Legendary item} obtained!"
# •	On the next three lines, print the remaining key materials
# •	On the several final lines, print the junk items
# •	All materials should be printed in the format: "{material}: {quantity}"
# •	The output should be lowercase, except for the first letter of the legendary

### Version 1:

# def legendary_item(needed_items: list, gained_items: dict):
#     for item in needed_items:
#         if gained_items[item] >= 250:
#             gained_items[item] -= 250
#             if item == "shards":
#                 return "Shadowmourne obtained!"
#             elif item == "fragments":
#                 return "Valanyr obtained!"
#             elif item == "motes":
#                 return "Dragonwrath obtained!"
#
#
# key_materials = ["shards", "fragments", "motes"]
# inventory = dict.fromkeys(key_materials, 0)
# win_item = False
#
# while not win_item:
#     items = input().lower().split()
#     for index in range(0, len(items), 2):
#         item = items[index + 1]
#         item_count = int(items[index])
#         if item not in inventory:
#             inventory[item] = 0
#         inventory[item] += item_count
#
#         if inventory["shards"] >= 250 or inventory["fragments"] >= 250 or inventory["motes"] >= 250:
#             win_item = True
#             break
#
# print(legendary_item(key_materials, inventory))
# [print(f"{key}: {value}") for key, value in inventory.items()]


### Version 2:
def calc_inventory(input_items: list, inventory_dict: dict):
    for index in range(0, len(input_items), 2):
        item = input_items[index + 1]
        item_count = int(input_items[index])
        if item not in inventory:
            inventory_dict[item] = 0
        inventory_dict[item] += item_count
        if inventory_dict["shards"] >= 250 or inventory_dict["fragments"] >= 250 or inventory_dict["motes"] >= 250:
            return True


def legendary_item(needed_items: list, gained_items: dict):
    for item in needed_items:
        if gained_items[item] >= 250:
            gained_items[item] -= 250
            if item == "shards":
                return "Shadowmourne obtained!"
            elif item == "fragments":
                return "Valanyr obtained!"
            elif item == "motes":
                return "Dragonwrath obtained!"


key_materials = ["shards", "fragments", "motes"]
inventory = dict.fromkeys(key_materials, 0)
win_item = False

while not win_item:
    items = input().lower().split()
    win_item = calc_inventory(items, inventory)

print(legendary_item(key_materials, inventory))
[print(f"{key}: {value}") for key, value in inventory.items()]
