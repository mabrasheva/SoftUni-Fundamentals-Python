# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints
# the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.


numbers = input()
numbers_list = list(map(int, numbers.split(", ")))

result = []
boundary = 10
while len(numbers_list) > 0:
    group_list = []
    min_number = min(numbers_list)
    if min_number > boundary:
        boundary += 10
    for number in numbers_list:
        if number in range(boundary - 9, boundary + 1):  # 1-10 -> 10's; 11-20 -> 20's
            group_list.append(number)
    for number in group_list:
        numbers_list.remove(number)

    result.append(f"Group of {boundary}'s: {group_list}")
print(*result, sep="\n")
