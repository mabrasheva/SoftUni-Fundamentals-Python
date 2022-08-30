# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

# Version 1:
#
# numbers = input().split(", ")
# even_numbers_indexes = []
#
#
# def even_number(i):
#     if i % 2 == 0:
#         return True
#
#
# for index, number in enumerate(numbers):
#     if even_number(int(number)):
#         even_numbers_indexes.append(index)
#
# print(even_numbers_indexes)

# Version 2:

numbers_list = list(map(int, input().split(", ")))

even_numbers_indexes = [index for index in range(len(numbers_list)) if numbers_list[index] % 2 == 0]
print(even_numbers_indexes)
