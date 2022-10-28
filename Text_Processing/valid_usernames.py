# Write a program that reads usernames on a single line (separated by ", ") and prints all valid usernames on separate lines.
# A valid username:
# •	has length between 3 and 16 characters inclusive
# •	can contain only letters, numbers, hyphens, and underscores
# •	has no redundant symbols before, after, or in between

def valid_length(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def valid_characters(username: str):
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def redundant_symbols(username):
    if " " not in username:
        return True
    return False


def valid_username(username):
    if valid_length(username) and valid_characters(username) and redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")

result = []
for user in usernames:
    if valid_username(user):
        result.append(user)
print(*result, sep="\n")
