# On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
# •	"Add Stop:{index}:{string}":
# o	Insert the given string at that index only if the index is valid
# •	"Remove Stop:{start_index}:{end_index}":
# o	Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
# •	"Switch:{old_string}:{new_string}":
# o	If the old string is in the initial string, replace it with the new one (all occurrences)
# Note: After each command, print the current state of the string if it is valid!
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
# •	JavaScript: you will receive a list of strings
# •	An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description

def add_stop(command: list, stops: str):
    index, string = int(command[1]), command[2]
    if 0 <= index < len(stops):
        stops = stops[:index] + string + stops[index::]
    return stops


def remove_stops(command: list, stops: str):
    start_index, end_index = int(command[1]), int(command[2])
    if 0 <= start_index <= end_index < len(stops):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch_stops(command: list, stops: str):
    old_string, new_string = command[1], command[2]
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


stops = input()
command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        stops = add_stop(command, stops)
    elif action == "Remove Stop":
        stops = remove_stops(command, stops)
    elif action == "Switch":
        stops = switch_stops(command, stops)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
