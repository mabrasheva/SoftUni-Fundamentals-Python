# You will be given a number. Print the largest number that can be formed from the digits of the given number.

number = int(input())
list_digits = []

for digit in (str(number)):
    list_digits.append(digit)
    list_digits.sort(reverse=True)
print(''.join(list_digits))
