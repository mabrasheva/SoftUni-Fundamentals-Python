# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for
# your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by
# a single space in the following format:
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. You will be receiving different
# commands, each on a new line, separated by " – ", until the "End" command is given.
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
# (the MP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100),
# HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"
# Input
# •	On the first line of the standard input, you will receive an integer n
# •	On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a
# space in the following format
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output
# •	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2
# spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"
# Constraints
# •	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective
# limits.
# •	The HP/MP amounts in the commands will never be negative.
# •	The hero names in the commands will always be valid members of your party. No need to check that explicitly.

def cast_spell(command: str):
    action, hero_name, mp_needed, spell_name = command.split(" - ")
    mp_needed = int(mp_needed)
    if heroes[hero_name]["mp"] >= mp_needed:
        heroes[hero_name]["mp"] -= mp_needed
        print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["mp"]} MP!')
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(command: str):
    action, hero_name, damage, attacker = command.split(" - ")
    heroes[hero_name]["hp"] -= int(damage)
    if heroes[hero_name]["hp"] > 0:
        print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]["hp"]} HP left!')
    else:
        del heroes[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(command: str):
    max_mp = 200
    action, hero_name, amount = command.split(" - ")
    amount = int(amount)
    if heroes[hero_name]["mp"] + amount > max_mp:
        amount_recovered = max_mp - heroes[hero_name]["mp"]
        heroes[hero_name]["mp"] = max_mp
    else:
        heroes[hero_name]["mp"] += amount
        amount_recovered = amount
    print(f"{hero_name} recharged for {amount_recovered} MP!")


def heal(command: str):
    max_hp = 100
    action, hero_name, amount = command.split(" - ")
    amount = int(amount)

    if heroes[hero_name]["hp"] + amount > max_hp:
        amount_recovered = max_hp - heroes[hero_name]["hp"]
        heroes[hero_name]["hp"] = max_hp
    else:
        heroes[hero_name]["hp"] += amount
        amount_recovered = amount
    print(f"{hero_name} healed for {amount_recovered} HP!")


heroes_count = int(input())
heroes = {}

for hero in range(heroes_count):
    name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    heroes[name] = {"hp": hp, "mp": mp}

command = input()
while command != "End":
    if command.startswith("CastSpell"):
        cast_spell(command)
    elif command.startswith("TakeDamage"):
        take_damage(command)
    elif command.startswith("Recharge"):
        recharge(command)
    elif command.startswith("Heal"):
        heal(command)

    command = input()

if heroes:
    for hero in heroes:
        print(f'{hero}\n  HP: {heroes[hero]["hp"]}\n  MP: {heroes[hero]["mp"]}')
