import re


def check_password(password: str):
    pattern = re.compile(
        r"^(.*)>(?P<numbers>\d{3})\|(?P<lower>[a-z]{3})\|(?P<upper>[A-Z]{3})\|(?P<symbols>[^<>]{3})<\1$")
    match = re.search(pattern, password)
    if match:
        encrypted_password = match["numbers"] + match["lower"] + match["upper"] + match["symbols"]
        print(f"Password: {encrypted_password}")
    else:
        print("Try another password!")


count = int(input())

for line in range(count):
    password = input()
    check_password(password)
