# Write a program to check if a number is prime.
# A prime number is a natural number greater than 1, not a product of two smaller natural numbers.
# For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
# The input comes as an integer number.
# The output should be True if the number is prime and False otherwise.

# Version 1:

number = int(input())
number_is_prime = True

counter = 0
for divider in range(1, 9 + 1):
    if number % divider == 0:
        counter += 1
        if counter > 2:
            number_is_prime = False
            break

print(bool(number_is_prime))

# Version 2:

# from sympy import isprime
#
# number = int(input())
#
# if isprime(number):
#     number_is_prime = True
# else:
#     number_is_prime = False
# print(bool(number_is_prime))
