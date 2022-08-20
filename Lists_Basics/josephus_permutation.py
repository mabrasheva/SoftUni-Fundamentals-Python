# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# •	the list itself - numbers separated by a single space representing the people in the circle
# •	a number k
# People are standing in a circle waiting to be executed. Counting begins from the first one in the circle and proceeds
# from left to right. After a specified number of people are skipped, the k person is executed. The procedure is
# repeated with the remaining people, starting with the next person, going in the same direction, and skipping the same
# number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"

numbers_list = input().split()
k_number = int(input())
result = []

index = 0
counter = 0

while len(numbers_list) > 0:
    counter += 1
    if counter % k_number == 0:
        result.append(numbers_list.pop(index))
    else:
        index += 1

    if index >= len(numbers_list):
        index = 0

result = [int(i) for i in result]
print(str(result).replace(" ", ""))
