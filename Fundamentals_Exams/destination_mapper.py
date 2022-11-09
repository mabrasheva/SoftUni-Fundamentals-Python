# You will be given a string representing some places on the map. You have to filter only the valid ones.
# A valid location is:
# •	Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
# •	After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be upper
# or lower-case)
# •	The letters must be at least 3
# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
# After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing
# the lengths of all the valid destinations that you have found on the map.
# In the end, on the first line, print: "Destinations: {destinations joined by ', '}".
# On the second line, print "Travel Points: {travel_points}".
# Input / Constraints
# •	You will receive a string representing the locations on the map
# •	JavaScript: you will receive a single parameter: string
# Output
# •	Print the messages described above

import re

places = input()
destinations = []
pattern = re.compile(r"([=\/])(?P<place>[A-Z][A-Za-z]{2,})\1")

matches = re.finditer(pattern, places)

if matches:
    for match in matches:
        destinations.append(match["place"])

travel_points = sum([len(destination) for destination in destinations])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
