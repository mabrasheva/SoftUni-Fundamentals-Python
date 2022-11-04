# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase".
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}".
# The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price.
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

import re

pattern = r">>([A-Za-z]+)<<([1-9][0-9]*?\.?\d*)\!(\d+)"
furniture_list = []
total_cost = 0

furniture = input()
while furniture != "Purchase":
    match = re.search(pattern, furniture)
    if match:
        furniture_name, price, quantity = match.groups()
        furniture_list.append(furniture_name)
        total_cost += float(price) * int(quantity)
    furniture = input()

print("Bought furniture:")
if furniture_list:
    print(*furniture_list, sep="\n")
print(f"Total money spend: {total_cost:.2f}")
