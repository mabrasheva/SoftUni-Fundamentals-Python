# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a
# list. Use abs().

def abs_value_list(input_list):
    final_list = []
    for element in input_list:
        number = abs(float(element))
        final_list.append(number)
    return final_list


current_list = input().split()
print(abs_value_list(current_list))
