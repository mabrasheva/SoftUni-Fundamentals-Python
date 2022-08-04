# Beaches are filled with sand, water, fish, and sun.
# Given a string, calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).

string = input().lower()
count = 0

count += string.count("sand")
count += string.count("water")
count += string.count("fish")
count += string.count("sun")

print(count)
