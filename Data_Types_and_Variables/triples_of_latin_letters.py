# Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:

number = int(input())

for first_letter in range(number):
    for second_letter in range(number):
        for third_letter in range(number):
            print(f"{chr(97 + first_letter)}{chr(97 + second_letter)}{chr(97 + third_letter)}")
