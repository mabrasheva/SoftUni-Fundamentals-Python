def new_follower(name: str):
    if name not in followers:
        followers[name] = 0


def like(name: str, number: int):
    if name not in followers:
        followers[name] = 0
    followers[name] += number


def comment(name: str):
    if name not in followers:
        followers[name] = 0
    followers[name] += 1


def blocked(name: str):
    if name in followers:
        del followers[name]
    else:
        print(f"{name} doesn't exist.")


followers = {}

command = input()
while command != "Log out":
    command = command.split(": ")
    action, username = command[0], command[1]

    if action == "New follower":
        new_follower(username)
    elif action == "Like":
        count = int(command[2])
        like(username, count)
    elif action == "Comment":
        comment(username)
    elif action == "Blocked":
        blocked(username)

    command = input()

print(f"{len(followers)} followers")
for user, likes in followers.items():
    print(f"{user}: {likes}")
