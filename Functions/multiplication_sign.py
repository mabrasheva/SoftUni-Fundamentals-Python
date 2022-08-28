# You will receive three integer numbers.
# Write a program that finds if their multiplication (the result) is negative, positive, or zero.
# Try to do this WITHOUT multiplying the 3 numbers.

def multiplication_sign(first, second, third):
    list_numbers = [first, second, third]

    if 0 in list_numbers:
        return "zero"

    counter_negative_numbers = 0
    for number in list_numbers:
        if number < 0:
            counter_negative_numbers += 1

    if counter_negative_numbers == 0:
        return "positive"
    elif counter_negative_numbers == 1:
        return "negative"
    elif counter_negative_numbers == 2:
        return "positive"
    elif counter_negative_numbers == 3:
        return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_sign(first_number, second_number, third_number))
