# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp."
# o	After that, print your current health: "Current health: {health} hp."
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case, you are facing a monster, which you will fight.
# The second part of the room contains the attack of the monster.
# You should remove the monster's attack from your health.
# o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# o	If you've died, print "You died! Killed by {monster}." and your quest is over.
# Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"
# Input / Constraints
# You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
# Output
# Print the corresponding messages described above.

def potion(value_to_add, health_value):
    if health_value + value_to_add >= 100:
        temp_health = health_value
        health_value = 100
        value_to_add = health_value - temp_health
    else:
        health_value += value_to_add
    print(f"You healed for {value_to_add} hp.")
    print(f"Current health: {health_value} hp.")
    return health_value


initial_health = 100
bitcoins = 0
health = initial_health
dead = False

rooms = input().split("|")
for room_index in range(len(rooms)):
    rooms[room_index] = rooms[room_index].split()
    command = rooms[room_index][0]
    number = int(rooms[room_index][1])

    if command == "potion":
        health = potion(number, health)

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if not health <= 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            dead = True
            print(f"Best room: {room_index + 1}")
            break

if not dead:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
