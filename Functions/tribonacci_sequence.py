# In the Tribonacci sequence, every number is formed by the sum of the previous 3.
# Write a function that prints numbers from the Tribonacci sequence on one line separated by a single space, starting
# from 1. You will receive a positive integer number as input.

def tribonacci_sequence(numbers_count):
    tribonacci_list = [1]
    for number in range(1, numbers_count):
        if len(tribonacci_list) < 3:
            tribonacci_list.append(number)
        else:
            tribonacci_list.append(sum(tribonacci_list[-3::]))
    return tribonacci_list


numbers_count_input = int(input())
print(tribonacci_sequence(numbers_count_input))
