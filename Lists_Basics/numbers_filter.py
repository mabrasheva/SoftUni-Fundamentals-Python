# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even).
# Finally, print the result.

numbers_count = int(input())
even = list()
odd = list()
negative = list()
positive = list()

for line in range(numbers_count):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

category = input()  # even, odd, negative, positive

print(eval(category))
