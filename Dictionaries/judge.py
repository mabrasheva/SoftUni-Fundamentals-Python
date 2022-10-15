# You know the judge system, right?! Your job is to create a program similar to the Judge system.
# You will receive several input lines in one of the following formats:
# "{username} -> {contest} -> {points}"
# The "contest" and "username" are strings, the given "points" will be an integer number.
# You need to keep track of every contest and points of each user:
# •	If the user has already participated in the contest, update their points only if the new ones are more than the
# older ones.
# •	Otherwise, just save the data - contest, username, and points.
# Also, you need to keep individual statistics for each user - his/her final total points for all contests.
# You should end your program when you receive the command "no more time".
# At that point, you should print each contest in order of input, for each contest print the participants ordered by
# points in descending order, then ordered by name in ascending order.
# After that, you should print individual statistics for every participant ordered by total points in descending order,
# and then by alphabetical order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Username and contest name always will be one word.
# •	Points will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	If all sorting criteria fail, the order should be by order of input.
# •	The input ends when you receive the command "no more time".
# Output
# •	The output format for the contests is:
# "{constest_name}: {number_participants} participants
# 1. {username1} <::> {points}
# 2. {username2} <::> {points}
# …
# {N}. {usernameN} <::> {points}"
# •	After you print all contests, print the individual statistics for every participant.
# •	The output format is:
# "Individual standings:
# 1.	{username1} -> {total_points}
# 2.	{username} -> {total_points}
# …
# {N}. {username} -> {total_points}"

def calc_contests(input_username: str, input_contest: str, input_points: int):
    add_points_to_user = True
    if input_contest not in contests:
        contests[input_contest] = {input_username: input_points}
    else:
        if input_username not in contests[input_contest]:
            contests[input_contest].update({input_username: input_points})
        else:
            if input_points > contests[input_contest][input_username]:
                # subtract the last points value, then with add_points_to_user adds the new points value.
                users[input_username] -= contests[input_contest][input_username]
                contests[input_contest].update({input_username: input_points})

            else:
                add_points_to_user = False

    if add_points_to_user:
        if input_username not in users:
            users[input_username] = 0
        users[input_username] += input_points

    return contests


users = {}
contests = {}
command = input()
while command != "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    calc_contests(username, contest, points)
    command = input()

for key, value in contests.items():
    print(f"{key}: {len(value)} participants")
    counter = 0
    for sub_key, sub_value in sorted(value.items(), key=lambda item: (-item[1], item[0])):
        counter += 1
        print(f"{counter}. {sub_key} <::> {sub_value}")

print("Individual standings:")
counter = 0
for key, value in sorted(users.items(), key=lambda item: (-item[1], item[0])):
    counter += 1
    print(f"{counter}. {key} -> {value}")
