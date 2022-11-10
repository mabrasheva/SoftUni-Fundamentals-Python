# On the first line, you will receive a number n.
# On the next n lines, you will be given some information about the plants that you have discovered in the format:
# "{plant}<->{rarity}". Store that information because you will need it later.
# If you receive a plant more than once, update its rarity.
# After that, until you receive the command "Exhibition", you will be given some of these commands:
# •	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
# •	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
# •	"Reset: {plant}" – remove all the ratings of the given plant
# Note: If any given plant name is invalid, print "error"
# After the command "Exhibition", print the information that you have about the plants in the following format:
# "Plants for the exhibition:
# - {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
# - {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
# …
# - {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
# The average rating should be formatted to the second decimal place.

def rate(plant: str, rating: int):
    if plant in plants:
        plants[plant]["Rating"].append(rating)
    else:
        print("error")
    return plants


def update(plant: str, new_rarity: int):
    if plant in plants:
        plants[plant]["Rarity"] = new_rarity
    else:
        print("error")
    return plants


def reset(plant: str):
    if plant in plants:
        plants[plant]["Rating"] = []
    else:
        print("error")
    return plants


count = int(input())
plants = {}

for line in range(count):
    plant, rarity = input().split("<->")
    plants[plant] = {"Rarity": int(rarity), "Rating": []}

command = input()
while command != "Exhibition":
    command = command.split(": ")
    action = command[0]
    if action == "Rate":
        plant, rating = command[1].split(" - ")
        plants = rate(plant, int(rating))
    elif action == "Update":
        plant, new_rarity = command[1].split(" - ")
        plants = update(plant, int(new_rarity))
    elif action == "Reset":
        plant = command[1]
        plants = reset(plant)
    command = input()

print("Plants for the exhibition:")
for plant in plants:
    if len(plants[plant]['Rating']):
        average_rating = sum(plants[plant]['Rating']) / len(plants[plant]['Rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plants[plant]['Rarity']}; Rating: {average_rating:.2f}")
