"""
Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in
the sequence, sorted in descending order.
Input
•	Read from the console a single line holding space-separated integers.
Output
•	Print the above-described numbers on a single line, space-separated.
•	If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
•	Print "No" if no numbers hold the above property.
Constraints
•	All input numbers are integers in the range [-1 000 000 … 1 000 000].
•	The count of numbers is in the range [1…10 000].
"""

numbers_as_string = input().split()
numbers = list(map(int, numbers_as_string))
numbers = sorted(numbers)
average = sum(numbers) / len(numbers)

# Syntax 1:

result = [number for number in numbers[-1:-6:-1] if number > average]

# Syntax 2:

# result = []
# for number in numbers[-1:-6:-1]:
#     if number > average:
#         result.append(number)

if len(result) == 0:
    print("No")

print(*result)
