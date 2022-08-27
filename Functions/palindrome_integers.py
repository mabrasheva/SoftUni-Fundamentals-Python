# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def is_palindrome(number):
    if number == number[::-1]:
        return True
    return False


input_numbers = input().split(", ")

for element in input_numbers:
    print(is_palindrome(element))
