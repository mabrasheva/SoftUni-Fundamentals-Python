# Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and
# unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have
# been tasked to analyze the software of the virus and observe its actions on the data.
# You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII
# character except whitespace. Then you will begin receiving commands in one of the following formats:
# •	merge {startIndex} {endIndex}
# •	divide {index} {partitions}
# Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex. In other
# words, you should concatenate them.
# Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
# If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
# Every time you receive the divide command, you must divide the element at the given index into several small
# substrings with equal length. The count of the substrings should be equal to the given partitions.
# Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
# If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal
# lengths and make the last one - the longest.
# Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
# The input ends when you receive the command "3:1". At that point, you must print the resulting elements, joined by a
# space.
# Input
# •	The first input line will contain the array of data.
# •	On the next several input lines, you will receive commands in the format specified above.
# •	The input ends when you receive the command "3:1".
# Output
# •	As output, you must print a single line containing the elements of the array, joined by a space.
# Constrains
# •	The strings in the array may contain any ASCII character except whitespace.
# •	The startIndex and the endIndex will be in the range [-1000…1000].
# •	The endIndex will always be greater than the startIndex.
# •	The index in the divide command will always be inside the array.
# •	The partitions will be in the range [0…100].
# •	Allowed working time/memory: 100ms / 16MB.

def merge(list_data, start, end):
    if end >= len(list_data):
        end = len(list_data) - 1

    if start < 0:
        start = 0

    for merge_index in range(start + 1, end + 1):
        list_data[start] += list_data[merge_index]
    for remove_index in range(end, start, -1):
        list_data.remove(list_data[remove_index])

    return list_data


def divide(list_data, index, number_of_partitions):
    string_to_divide = list_data[index]
    string_divided = list_data[index]
    if number_of_partitions > 0:
        length_of_each_partition = len(list_data[index]) // number_of_partitions
        remainder_to_add_to_the_last_partition = len(list_data[index]) % number_of_partitions
        for index_of_partition in range(index, index + number_of_partitions):
            partition_to_insert = string_divided[0:length_of_each_partition]
            list_data.insert(index_of_partition, partition_to_insert)
            string_divided = string_divided[length_of_each_partition::]
        if remainder_to_add_to_the_last_partition > 0:
            list_data[index + number_of_partitions - 1] = list_data[number_of_partitions - 1] + string_divided

        list_data.remove(string_to_divide)

    return list_data


input_data = input().split()
command = input().split()
action = command[0]
while action != "3:1":
    start_index = int(command[1])
    index = int(command[1])
    end_index = int(command[2])
    partitions = int(command[2])

    if action == "merge":
        merge(input_data, start_index, end_index)
    elif action == "divide":
        divide(input_data, index, partitions)

    command = input().split()
    action = command[0]

print(*input_data)
