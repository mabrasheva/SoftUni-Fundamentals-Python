# Write a program that reads four integer numbers.
# It should add the first to the second number, integer divide the sum by the third number,
# and multiply the result by the fourth number. Print the final result.

number_one = int(input())
number_two = int(input())
number_three = int(input())
number_four = int(input())

result = (number_one + number_two) // number_three * number_four
print(result)
