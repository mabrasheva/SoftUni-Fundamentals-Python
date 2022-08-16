# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following
# format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index}"
# o	If the index is valid, replace the gift on the given index with the given gift.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the
# following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# •	On the 1st line,  you will receive the names of the gifts, separated by a single space.
# •	On the following lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.
# Output
# •	Print the gifts in the format described above.

gifts = input().split()

command = input()
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":  # "OutOfStock {gift}"
        # Find the gifts with this name in your collection, if any, and change their values to "None".
        for index in range(len(gifts)):
            if command[1] == gifts[index]:
                gifts[index] = "None"
    elif command[0] == "Required":  # "Required {gift} {index}"
        # If the index is valid, replace the gift on the given index with the given gift.
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == "JustInCase":  # "JustInCase {gift}"
        # Replace the value of your last gift with this one.
        gifts[-1] = command[1]
    command = input()

# Print the gifts on a single line, except the ones with value "None", separated by a single space.
if "None" in gifts:
    for element in range(len(gifts) - 1, -1, -1):
        if "None" in gifts[element]:
            gifts.remove(gifts[element])

print(' '.join(gifts))
