# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info which will be some
# alphanumeric characters. In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is the
# distance he ran. So here we have George who ran 29 km. Store the information about the person only if the list of
# racers contains the name of the person. If you receive the same person more than once just add the distance to his
# old distance. At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"

import re

pattern_letter = r"[A-Z]|[a-z]"
pattern_digit = r"\d"
participants = input().split(", ")
statistics = {}

line = input()
while line != "end of race":
    name = re.findall(pattern_letter, line)
    name = "".join(name)
    if name in participants:
        distance = re.findall(pattern_digit, line)
        distance = [int(digit) for digit in distance]
        if distance:
            if name not in statistics:
                statistics[name] = 0
            statistics[name] += sum(distance)
    line = input()

statistics = sorted(statistics.items(), key=lambda item: item[1], reverse=True)
first_three = statistics[0:3]
winners = [winner[0] for winner in first_three]

place = 0
for winner in winners:
    place += 1
    if place == 1:
        print(f"1st place: {winner}")
    elif place == 2:
        print(f"2nd place: {winner}")
    elif place == 3:
        print(f"3rd place: {winner}")
