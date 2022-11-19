# Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels.
# Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and
# treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate's
# way!
# Until the "Sail" command is given, you will be receiving:
# •	You and your crew have targeted cities, with their population and gold, separated by "||".
# •	If you receive a city that has already been received, you have to increase the population and gold with the given
# values.
# After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given.
# Events will be in the following format:
# •	"Plunder=>{town}=>{people}=>{gold}"
# o	You have successfully attacked and plundered the town, killing the given number of people and stealing the
# respective amount of gold.
# o	For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
# o	If any of those two values (population or gold) reaches zero, the town is disbanded.
# 	You need to remove it from your collection of targeted cities and print the following message: "{town} has been
# wiped off the map!"
# o	There will be no case of receiving more people or gold than there is in the city.
# •	"Prosper=>{town}=>{gold}"
# o	There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
# o	The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added
# cannot be a negative number!" and ignore the command.
# o	If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the
# following message:
# "{gold added} gold added to the city treasury. {town} now has {total gold} gold."
# Input
# •	On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold
# and population, separated by "||"
# •	On the following lines, until the "End" command, you will be receiving strings representing the actions described
# above, separated by "=>"
# Output
# •	After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print
# all of them, in the following format:
# "Ahoy, Captain! There are {count} wealthy settlements to go to:
# {town1} -> Population: {people} citizens, Gold: {gold} kg
# {town2} -> Population: {people} citizens, Gold: {gold} kg
#    …
# {town…n} -> Population: {people} citizens, Gold: {gold} kg"
# •	If there are no settlements left to plunder, print:
# "Ahoy, Captain! All targets have been plundered and destroyed!"
# Constraints
# •	The initial population and gold of the settlements will be valid 32-bit integers, never negative, or exceed the
# respective limits.
# •	The town names in the events will always be valid towns that should be on your list.

def plunder(town: str, people: int, gold: int):
    cities[town]["population"] -= people
    cities[town]["gold"] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities[town]["population"] == 0 or cities[town]["gold"] <= 0:
        print(f"{town} has been wiped off the map!")
        del cities[town]


def prosper(town: str, gold: int):
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[town]["gold"] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')


cities = {}

command = input()
while command != "Sail":
    city, population, gold = command.split("||")
    if city not in cities:
        cities[city] = {"population": 0, "gold": 0}
    cities[city]["population"] += int(population)
    cities[city]["gold"] += int(gold)
    command = input()

line = input()
while line != "End":
    line = line.split("=>")
    action, town = line[0], line[1]
    if action == "Plunder":
        people, gold = int(line[2]), int(line[3])
        plunder(town, people, gold)
    elif action == "Prosper":
        gold = int(line[2])
        prosper(town, gold)
    line = input()

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities:
        print(f'{town} -> Population: {cities[town]["population"]} citizens, Gold: {cities[town]["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
