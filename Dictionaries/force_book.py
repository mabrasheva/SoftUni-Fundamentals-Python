# The force users struggle to remember which side is the different force users from because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the
# corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side.
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side.
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the
# corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force
# side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	The input ends when you receive the command "Lumpawaroo".
# Output
# •	As output for each force side, you must print all the force users.
# •	The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}
# ! {force_user2}
# …
# ! {force_userN}"
# •	In case there are NO force users on a side, don't print this side.

def add_user(side: str, user: str):
    if side not in force_dict:
        force_dict[side] = []
    adding_user = True
    for key in force_dict:
        if user in force_dict[key]:
            adding_user = False
            break
    if adding_user:
        force_dict[side].append(user)
    return force_dict


def add_user_or_swap_side(side: str, user: str):
    if side not in force_dict:
        force_dict[side] = []
    for key in force_dict:
        if user in force_dict[key]:
            force_dict[key].remove(user)
    force_dict[side].append(user)
    print(f"{force_user} joins the {force_side} side!")
    return force_dict


force_dict = {}

command = input()
while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")
        add_user(force_side, force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        add_user_or_swap_side(force_side, force_user)

    command = input()

for side, users in force_dict.items():
    members = len(force_dict[side])
    if members:
        print(f"Side: {side}, Members: {members}")
        for user in users:
            print(f"! {user}")
