# Wolves have been reintroduced to Great Britain.
# You are a sheep farmer and are now plagued by wolves who pretend to be sheep.
# Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep".
# Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!"
#       where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
# Input
# The input will be a single string containing the animals separated by a comma and a single space ", "

string_animals = input()
list_animals = string_animals.split(", ")

for number in range(len(list_animals), 0, -1):
    # print(number, end=" ")
    # print(list_animals[-number])
    if list_animals[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif list_animals[-number] == "wolf":
        print(f"Oi! Sheep number {number - 1}! You are about to be eaten by a wolf!")
