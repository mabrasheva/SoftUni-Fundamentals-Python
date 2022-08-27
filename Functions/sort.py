# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

def sorted_numbers(list_numbers):
    return sorted(list_numbers)


input_string = input().split()
input_numbers = [int(i) for i in input_string]

print(sorted_numbers(input_numbers))
