# Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line, you will
# receive the status of the pirate ship, which is a string representing integer sections separated by ">".
# On the second line, you will receive the same type of status, but for the warship:
# "{section1}>{section2}>{section3}… {sectionn}"
# On the third line, you will receive the maximum health capacity a section of the ship can reach.
# The following lines represent commands until "Retire":
# •	"Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the
# index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks, print the
# following and stop the program: "You won! The enemy ship has sunken."
# •	"Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range
# (indexes are inclusive). Check if both indexes are valid and if not, skip the command.
# If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
# "You lost! The pirate ship has sunken."
# •	"Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index
# is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
# •	"Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that
# are lower than 20% of the maximum health capacity. Print the following:
# "{count} sections need repair."
# In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in
# the following format:
# "Pirate ship status: {pirateShipSum}
# Warship status: {warshipSum}"
# Input
# •	On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
# •	On the 2nd line, you are going to receive the status of the warship
# •	On the 3rd line, you will receive the maximum health a section of a ship can reach.
# •	On the following lines, until "Retire", you will be receiving commands.
# Output
# •	Print the output in the format described above.
# Constraints
# •	The section numbers will be integers in the range [1….1000]
# •	The indexes will be integers [-200….200]
# •	The damage will be an integer in the range [1….1000]
# •	The health will be an integer in the range [1….1000]


status_pirate_ship = input().split(">")
status_pirate_ship = list(map(int, status_pirate_ship))
status_warship = input().split(">")
status_warship = list(map(int, status_warship))
max_health = int(input())

command = input()
while command != "Retire":
    command = command.split()
    action = command[0]

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index <= end_index < len(status_pirate_ship):
            for index in range(start_index, end_index + 1):
                status_pirate_ship[index] -= damage
                if status_pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(status_pirate_ship):
            status_pirate_ship[index] += health
            if status_pirate_ship[index] > max_health:
                status_pirate_ship[index] = max_health
    elif action == "Status":
        low_health = 0.20 * max_health
        count = 0
        for section in status_pirate_ship:
            if section < low_health:
                count += 1
        print(f"{count} sections need repair.")

    command = input()

if sum(status_pirate_ship) > 0 and sum(status_warship) > 0:
    print(f"Pirate ship status: {sum(status_pirate_ship)}")
    print(f"Warship status: {sum(status_warship)}")
