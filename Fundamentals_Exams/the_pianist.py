# You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it
# and add, change, remove pieces from it!
# On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
# On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following
# format: "{piece}|{composer}|{key}".
# Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is
# given:
# •	"Add|{piece}|{composer}|{key}":
# o	You need to add the given piece with the information about it to the other pieces and print:
# "{piece} by {composer} in {key} added to the collection!"
# o	If the piece is already in the collection, print:
# "{piece} is already in the collection!"
# •	"Remove|{piece}":
# o	If the piece is in the collection, remove it and print:
# "Successfully removed {piece}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# •	"ChangeKey|{piece}|{new key}":
# o	If the piece is in the collection, change its key with the given one and print:
# "Changed the key of {piece} to {new key}!"
# o	Otherwise, print:
# "Invalid operation! {piece} does not exist in the collection."
# Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
# "{Piece} -> Composer: {composer}, Key: {key}"
# Input/Constraints
# •	You will receive a single integer at first – the initial number of pieces in the collection
# •	For each piece, you will receive a single line of text with information about it.
# •	Then you will receive multiple commands in the way described above until the command "Stop".
# Output
# •	All the output messages with the appropriate formats are described in the problem description.

def add_piece(piece, composer, key, collection):
    if piece not in collection:
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return collection


def remove_piece(piece, collection):
    if piece in collection:
        del collection[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection


def change_key(piece, new_key, collection):
    if piece in collection:
        collection[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return collection


count = int(input())
collection = {}

for line in range(count):
    piece, composer, key = input().split("|")
    collection[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":
    command = command.split("|")
    action = command[0]
    if action == "Add":
        piece, composer, key = command[1], command[2], command[3]
        collection = add_piece(piece, composer, key, collection)
    elif action == "Remove":
        piece = command[1]
        collection = remove_piece(piece, collection)
    elif action == "ChangeKey":
        piece, new_key = command[1], command[2]
        collection = change_key(piece, new_key, collection)
    command = input()

for piece, info in collection.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
