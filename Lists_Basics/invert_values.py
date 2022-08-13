# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

initial_string = input().split()
opposite_list = []
for index in range(len(initial_string)):
    opposite_number = -int(initial_string[index])
    opposite_list.append(opposite_number)
print(opposite_list)
