# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all
# the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number


def positive(numbers_list):
    return [str(number) for number in numbers_list if number >= 0]


def negative(numbers_list):
    return [str(number) for number in numbers_list if number < 0]


def even(numbers_list):
    return [str(number) for number in numbers_list if number % 2 == 0]


def odd(numbers_list):
    return [str(number) for number in numbers_list if number % 2 != 0]


numbers = input()
numbers_as_digits = list(map(int, numbers.split(", ")))

positive_list = positive(numbers_as_digits)
negative_list = negative(numbers_as_digits)
even_list = even(numbers_as_digits)
odd_list = odd(numbers_as_digits)

print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")
