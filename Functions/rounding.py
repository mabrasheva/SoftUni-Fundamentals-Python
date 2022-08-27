# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

def round_function(list_floats: list):
    result_list = [round(element) for element in list_floats]
    # for element in list_floats:
    #     number = round(element)
    #     result_list.append(number)
    return result_list


input_list = input().split()
input_list = [float(i) for i in input_list]

print(round_function(input_list))
