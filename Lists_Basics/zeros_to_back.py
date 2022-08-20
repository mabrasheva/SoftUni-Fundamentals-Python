# Write a program that receives a single string (integers separated by a comma and space ", "),
# finds all the zeros, and moves them to the back without messing up the other elements.
# Print the resulting integer list.

list_numbers = input().split(", ")
list_numbers = [int(integer) for integer in list_numbers]
for number in list_numbers:
    if number == 0:
        list_numbers.remove(0)
        list_numbers.append(0)
print(list_numbers)
