# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list,
# separated by a comma and a space ", ".

list_of_integers = input().split()
count_of_numbers_to_remove = int(input())
list_of_integers = [int(integer) for integer in list_of_integers]

for number in range(count_of_numbers_to_remove):
    smallest = min(list_of_integers)
    list_of_integers.remove(smallest)

list_of_integers = [str(string) for string in list_of_integers]

print(', '.join(list_of_integers))
