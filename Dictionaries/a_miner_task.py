# You will be given a sequence of strings, each on a new line until you receive the "stop" command.
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

resources_dict = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource not in resources_dict.keys():
        resources_dict[resource] = 0
    resources_dict[resource] += quantity

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
