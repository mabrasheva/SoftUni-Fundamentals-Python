# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"

def min_max_sum(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    sum_numbers = sum(numbers)
    return f"The minimum number is {min_number}\nThe maximum number is {max_number}\nThe sum number is: {sum_numbers}"


input_numbers = input().split()
list_numbers = [int(i) for i in input_numbers]

print(min_max_sum(list_numbers))
