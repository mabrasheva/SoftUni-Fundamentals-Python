# Heroes III is the best game ever. Everyone loves it and everyone plays it all the time. Simon is no exclusion to this
# rule. His favorite units in the game are all types of dragons – black, red, gold, azure etc. He likes them so much
# that he gives them names and keeps logs of their stats: damage, health, and armor. The process of aggregating all the
# data is quite tedious, so he would like to have a program doing it. Since he is no programmer, it's your task to help
# him.
# You need to categorize dragons by their type. For each dragon, identified by name, keep information about his stats
# (damage, health, and armor). Type is preserved as in the order of input, but dragons are sorted alphabetically by
# their name. For each type, you should also print the average damage, health, and armor of the dragons. For each
# dragon, print his own stats.
# There may be missing stats in the input, though. If a stat is missing you should assign it default values. Default
# values are as follows: health 250, damage 45, and armor 10. Missing stat will be marked by "null".
# The input is in the following format "{type} {name} {damage} {health} {armor}".
# The "type" and the "name" are strings. The "damage", the "health", and the "armor" are integers. Any of the integers
# may be assigned "null" value. See the examples below for better understanding of your task.
# If the same dragon is added a second time, the new stats should overwrite the previous ones. Two dragons are
# considered equal if they match by both name and type.
# Input
# •	On the first line, you are given number N -> the number of dragons to follow.
# •	On the next N lines, you are given input in the above-described format. There will be a single space separating each
# element.
# Output
# •	Print the aggregated data on the console.
# •	For each type, print average stats of its dragons in format "{type}::({damage}/{health}/{armor})".
# •	Damage, health, and armor should be rounded to two digits after the decimal separator.
# •	For each dragon, print its stats in format "-{Name} -> damage: {damage}, health: {health}, armor: {armor}".
# Constraints
# •	N is in range [1…100].
# •	The dragon type and name are one word only, starting with capital letter.
# •	Damage health and armor are integers in range [0 … 100000] or null.

def dragons(color, dragon_name, dragon_damage, dragon_health, dragon_armor):
    if dragon_damage == "null":
        dragon_damage = 45
    if dragon_health == "null":
        dragon_health = 250
    if dragon_armor == "null":
        dragon_armor = 10
    dragon_damage, dragon_health, dragon_armor = int(dragon_damage), int(dragon_health), (int(dragon_armor))

    if color not in dict_dragons:
        dict_dragons[color] = {dragon_name: [dragon_damage, dragon_health, dragon_armor]}
    else:
        if dragon_name not in dict_dragons[color]:
            dict_dragons[color].update({dragon_name: [dragon_damage, dragon_health, dragon_armor]})
        else:
            dict_dragons[color][dragon_name] = [dragon_damage, dragon_health, dragon_armor]

    return dict_dragons


dict_dragons = {}
dragons_count = int(input())
for element in range(dragons_count):
    dragon = input()
    dragon_type, name, damage, health, armor = dragon.split()
    dict_dragons = dragons(dragon_type, name, damage, health, armor)

for key, name_dragon in dict_dragons.items():
    total_damage_list = []
    total_health_list = []
    total_armor_list = []
    for value in name_dragon.values():
        total_damage_list.append(value[0])
        total_health_list.append(value[1])
        total_armor_list.append(value[2])
    total_damage = sum(total_damage_list)
    total_health = sum(total_health_list)
    total_armor = sum(total_armor_list)
    count = len(name_dragon)
    avg_damage = total_damage / count
    avg_health = total_health / count
    avg_armor = total_armor / count

    print(f"{key}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for sub_key, stats in sorted(name_dragon.items()):
        damage = stats[0]
        health = stats[1]
        armor = stats[2]
        print(f"-{sub_key} -> damage: {damage}, health: {health}, armor: {armor}")
