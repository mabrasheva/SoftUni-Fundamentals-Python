# Write a program that decrypts a message by a given key and gathers information about hidden treasure type and its
# coordinates. On the first line, you will receive a key (sequence of numbers separated by a space). On the next few
# lines, you will receive lines with strings until you get the command "find".
# You should loop through every string and decrease the ASCII code of each character with a corresponding number of the
# key sequence. You choose a key number from the sequence by just looping through it. If the length of the key sequence
# is less than the string sequence, you should continue looping from the beginning.
# For more clarification, see the example below.
# After decrypting the message, you will get a type of treasure and its coordinates. The type will be between the symbol
# "&", and the coordinates - between the symbols "<' and '>'.
# For each line print the type and the coordinates in the format "Found {type} at {coordinates}".

key = list(map(int, input().split()))
result = ""

command = input()
while command != "find":

    for index, character in enumerate(command):
        if index < len(key):
            key_index = index
        else:
            key_index = index % len(key)
        result += chr(ord(command[index]) - key[key_index])

    treasure_indexes = {"start_index": 0, "end_index": 0}
    coordinates_indexes = {"start_index": 0, "end_index": 0}
    for sub_index, sub_character in enumerate(result):
        if sub_character == "&":
            if treasure_indexes["start_index"] == 0:
                treasure_indexes["start_index"] = sub_index + 1
            elif treasure_indexes["end_index"] == 0:
                treasure_indexes["end_index"] = sub_index
        elif sub_character == "<" or sub_character == ">":
            if coordinates_indexes["start_index"] == 0:
                coordinates_indexes["start_index"] = sub_index + 1
            elif coordinates_indexes["end_index"] == 0:
                coordinates_indexes["end_index"] = sub_index

    treasure = result[treasure_indexes["start_index"]:treasure_indexes["end_index"]]
    coordinates = result[coordinates_indexes["start_index"]:coordinates_indexes["end_index"]]

    result = ""
    print(f"Found {treasure} at {coordinates}")
    command = input()
