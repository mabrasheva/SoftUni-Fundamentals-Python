import sys

number_one = int(input())
number_two = int(input())
number_three = int(input())
largest_number = -sys.maxsize

if number_one > number_two and number_one > number_three:
    largest_number = number_one
elif number_two > number_one and number_two > number_three:
    largest_number = number_two
else:
    largest_number = number_three

print(largest_number)