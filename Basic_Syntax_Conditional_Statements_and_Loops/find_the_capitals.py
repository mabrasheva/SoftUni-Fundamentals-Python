# Write a program that takes a single string and prints a list of all the capital letters indices.

string = input()
index_list = []

for index, letter in enumerate(string):
    if letter.isupper():
        index_list.append(index)

print(index_list)
