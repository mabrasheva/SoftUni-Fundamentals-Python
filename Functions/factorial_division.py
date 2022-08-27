# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

from math import factorial


def calculate_factorial(number):
    return factorial(number)


first_number = int(input())
second_number = int(input())

result = calculate_factorial(first_number) // calculate_factorial(second_number)

print(f"{result:.2f}")
