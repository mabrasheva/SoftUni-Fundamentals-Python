"""
Write a program that keeps track of every won battle against an enemy. You will receive initial energy. Afterward, you
will start receiving the distance you need to reach an enemy until the "End of battle" command is given, or you run out
of energy.
The energy you need for reaching an enemy is equal to the distance you receive. Each time you reach an enemy, you win a
battle, and your energy is reduced. Otherwise, if you don't have enough energy to reach an enemy, end the program and
print: "Not enough energy! Game ends with {count} won battles and {energy} energy".
Every third won battle increases your energy with the value of your current count of won battles.
Upon receiving the "End of battle" command, print the count of won battles in the following format:
"Won battles: {count}. Energy left: {energy}"
Input / Constraints
•	On the first line, you will receive initial energy – an integer [1-10000].
•	On the following lines, you will be receiving the distance of an enemy – an integer [1-10000]
Output
•	The description contains the proper output messages for each case and the format they should be printed.
"""

initial_energy = int(input())
current_energy = initial_energy
out_of_energy = False
wins = 0
distance = input()

while distance != "End of battle":
    distance = int(distance)

    if current_energy >= distance:
        wins += 1
        current_energy -= distance
        if wins % 3 == 0:
            current_energy += wins
    else:
        out_of_energy = True
        break

    distance = input()

if out_of_energy:
    print(f"Not enough energy! Game ends with {wins} won battles and {current_energy} energy")
elif distance == "End of battle":
    print(f"Won battles: {wins}. Energy left: {current_energy}")
