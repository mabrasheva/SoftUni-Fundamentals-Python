# Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma
# and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", ").
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".

### Version 1:

# countries = input().split(", ")
# capitals = input().split(", ")
#
# result = dict(zip(countries, capitals))
#
# for country, capital in result.items():
#     print(f"{country} -> {capital}")

### Version 2:

# countries = input().split(", ")
# capitals = input().split(", ")
#
# result = {}
# for index in range(len(countries)):
#     result[countries[index]] = capitals[index]
#
# [print(f"{country} -> {capital}") for country, capital in result.items()]

### Version 3:

countries = input().split(", ")
capitals = input().split(", ")

result = {countries[index]: capitals[index] for index in range(len(countries))}

[print(f"{country} -> {capital}") for country, capital in result.items()]
