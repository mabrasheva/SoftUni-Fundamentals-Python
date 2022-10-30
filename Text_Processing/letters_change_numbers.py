# John invented a game with numbers and letters from the English alphabet. The game was simple.
# You receive a string consisting of a number between two letters. For the given string, you should perform different
# mathematical operations to achieve a result:
# •	First, if the letter in front of the number is:
# o	Uppercase: divide the number by the letter's position in the alphabet (starting from 1)
# o	Lowercase: multiply the number with the letter's position in the alphabet (starting from 1)
# •	Next, if the letter after the number is:
# o	Uppercase: subtract its position from the resulting number (starting from 1)
# o	Lowercase: add its position to the resulting number (starting from 1)
# The game was too easy for John. He decided to complicate it by doing the same calculations to multiple strings keeping
# track of only the total sum of all results. Once he started to solve this with more strings and bigger numbers, it
# became quite hard to do it only in his mind.
# He kindly asks you to write a program that performs the operations described above and sums the final results of each
# string.
# Input
# •	The input comes from the console as a single line, holding a sequence of strings
# •	Strings are separated by one or more white spaces
# •	The input data will always be valid. There is no need to check it explicitly
# Output
# •	Print at the console a single number:
# o	The total sum of all processed numbers, formatted to the second decimal separator
# Constraints
# •	The count of the strings will be in the range [1 … 10]
# •	The numbers between the letters will be integers in the range [1 … 2 147 483 647]
# •	Time limit: 0.3 sec. Memory limit: 16 MB

def sum_string(first, last, num):
    result = 0
    if first.isupper():
        position_first = ord(first) - 64
        result = num / position_first
    elif first.islower():
        position_first = ord(first) - 96
        result = num * position_first
    if last.isupper():
        position_last = ord(last) - 64
        result -= position_last
    elif last.islower():
        position_last = ord(last) - 96
        result += position_last
    return result


sequence = input().split()
total_sum = 0
for string in sequence:
    first_letter, last_letter = string[0], string[-1]
    # Find the number using isdigit:
    # number = [character for character in string if character.isdigit()]
    # number = int(("").join(number))
    # Find the number using slicing:
    # number = int(string[1:len(string) - 1])
    # Find the number using strip:
    number = int(string.lstrip(first_letter).rstrip(last_letter))
    result_number = sum_string(first_letter, last_letter, number)
    total_sum += result_number
print(f"{total_sum:.2f}")
