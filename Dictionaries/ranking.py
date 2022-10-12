# Here comes the final and the most interesting part – the Final ranking of the candidate-interns.
# The final ranking is determined by the points of the interview tasks and by the points from the exams in SoftUni.
# Here is your final task. You will receive some lines of input in the format "{contest}:{password for contest}" until
# you receive "end of contests". Save that data because you will need it later. After that you will receive other type
# of inputs in format "{contest}=>{password}=>{username}=>{points}" until you receive "end of submissions".
# Here is what you need to do.
# •	Check if the contest is valid (It is considered valid if you received it in the first type of input)
# •	Check if the password is correct for the given contest
# •	If the contest and the password is valid, save the user with the contest they take part in (a user can take part in
# many contests) and the points the user has in the given contest. If you receive the same contest and the same user
# update the points only if the new ones are more than the older ones.
# In the end, you should print the info for the user with the most points (total points for all contents they
# participated in) in the format "Best candidate is {user} with total {total_points} points.".
# After that print all students ordered by their names. For each user print each contest with the points in descending
# order. See the examples.
# Input
# •	Strings in format "{contest}:{password for contest}" until the "end of contests" command.
# There will be no case with two equal contests
# •	Strings in format "{contest}=>{password}=>{username}=>{points}" until the "end of submissions" command.
# •	There will be no case with 2 or more users with same total points!
# Output
# •	On the first line, print the best user in format "Best candidate is {user} with total {total points} points.".
# •	Then print all students ordered as mentioned above in format:
# "{user_name1}
# #  {contest1} -> {points}
# #  {contest2} -> {points}
# …
# #  {contestN} -> {points}"
# Constraints
# •	The strings may contain any ASCII character except from (:, =, >).
# •	The numbers will be in range [0 - 10000].
# •	Second input is always valid.

def check_user(contest, password, username, points):
    points = int(points)
    if contest in contests and password == contests[contest]:
        if username not in users:
            users[username] = {contest: points}
        else:
            if contest in users[username]:
                if points > users[username][contest]:
                    users[username].update({contest: points})  # users[username][contest] = {contest: points}
            else:
                users[username].update({contest: points})

    return users


contests = {}
max_points = 0
best_candidate = ""

command = input()
while command != "end of contests":
    existing_contest, password_for_contest = command.split(":")
    contests[existing_contest] = password_for_contest
    command = input()

users = {}
second_command = input()
while second_command != "end of submissions":
    input_contest, input_password, input_username, input_points = second_command.split("=>")
    users = check_user(input_contest, input_password, input_username, input_points)
    second_command = input()

for user, value in users.items():
    total_points = 0
    for contest, points in value.items():
        total_points += points

    if max_points < total_points:
        max_points = total_points
        best_candidate = user

users_sorted_names = {key: value for key, value in sorted(users.items())}
print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for user, value in users_sorted_names.items():
    print(user)
    for contest, points in sorted(value.items(), key=lambda item: -item[1]):
        print(f"#  {contest} -> {points}")
