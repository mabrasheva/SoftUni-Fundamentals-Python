# The list may be manipulated by one of the following commands:
# •	"exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists.
# E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
# o	If the index is outside the boundaries of the list, print "Invalid index"
# o	A negative index is considered invalid
# •	"max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
# •	"min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
# o	If there are two or more equal min/max elements, return the index of the rightmost one
# o	If a min/max even/odd element cannot be found, print "No matches"
# •	"first {count} even/odd" – returns the first count even/odd elements.
# E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
# •	"last {count} even/odd" – returns the last count even/odd elements.
# E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
# o	If the count is greater than the list length, print "Invalid count"
# o	If there are not enough elements to satisfy the count, print as many as you can.
# If there are zero even/odd elements, print an empty list "[]"
# •	"end" - stop taking input and print the final state of the list
# Input
# •	The input data should be read from the console.
# •	On the first line, the initial list is received as a line of integers, separated by a single space.
# •	On the following lines, until the command "end" is received, you will receive the list manipulation commands.
# •	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# •	The output should be printed on the console.
# •	On a separate line, print the output of the corresponding command.
# •	On the last line, print the final list in square brackets with its elements separated by a comma and a space.
# •	See the examples below to get a better understanding of your task.
# Constraints
# •	The number of input lines will be in the range [2 … 50].
# •	The list elements will be integers in the range [0 … 1000].
# •	The number of elements will be in the range [1 .. 50].
# •	The split index will be an integer in the range [-231 … 231 – 1].
# •	The first/last count will be an integer in the range [1 … 231 – 1].
# •	There will not be redundant whitespace anywhere in the input.
# •	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.

input_list = input().split()
current_list = input_list

command = input()
while command != "end":
    command = command.split()

    if command[0] == "exchange":
        exchange_index = int(command[1])
        # If the index is outside the boundaries of the list, print "Invalid index".
        # A negative index is considered invalid
        if exchange_index < 0 or exchange_index >= len(current_list):
            print("Invalid index")
        else:
            # "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting
            # sub-lists. E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
            left_temp_list = current_list[:exchange_index + 1]
            right_temp_list = current_list[exchange_index + 1:]
            current_list = right_temp_list + left_temp_list
            # print(current_list)

    else:
        even_list = []
        odd_list = []
        current_list = [int(i) for i in current_list]
        for number in current_list:
            if number % 2 == 0:
                even_list.append(number)
            else:
                odd_list.append(number)

        # If a min/max even/odd element cannot be found, print "No matches"
        if len(odd_list) == 0 and command[1] == "odd":
            print("No matches")
            command = input()
            continue
        elif len(even_list) == 0 and command[1] == "even":
            print("No matches")
            command = input()
            continue

        # Return the INDEX of the max/min even/odd element.
        # If there are two or more equal min/max elements, return the index of the rightmost one
        if command[0] == "max":
            if command[1] == "even":
                max_even = max(even_list)
                for element_index in range(len(current_list) - 1, -1, -1):
                    if max_even in current_list:
                        if max_even == current_list[element_index]:
                            max_even_index = element_index
                            print(max_even_index)
                            break

            elif command[1] == "odd":
                max_odd = max(odd_list)
                for element_index in range(len(current_list) - 1, -1, -1):
                    if max_odd in current_list:
                        if max_odd == current_list[element_index]:
                            max_odd_index = element_index
                            print(max_odd_index)
                            break

        elif command[0] == "min":
            if command[1] == "even":
                min_even = min(even_list)
                for element_index in range(len(current_list) - 1, -1, -1):
                    if min_even in current_list:
                        if min_even == current_list[element_index]:
                            min_even_index = element_index
                            print(min_even_index)
                            break

            elif command[1] == "odd":
                min_odd = min(odd_list)
                for element_index in range(len(current_list) - 1, -1, -1):
                    if min_odd in current_list:
                        if min_odd == current_list[element_index]:
                            min_odd_index = element_index
                            print(min_odd_index)
                            break

        # Returns the first/last count even/odd elements.
        # If the count is greater than the list length, print "Invalid count"
        elif command[0] == "first" or command[0] == "last":
            count = int(command[1])
            if count > len(current_list):
                print("Invalid count")
            else:
                if command[2] == "even":
                    # If there are not enough elements to satisfy the count, print as many as you can.
                    # If there are zero even/odd elements, print an empty list "[]"
                    if count >= len(even_list):
                        count = len(even_list)
                    if command[0] == "first":
                        print(even_list[:count])
                    elif command[0] == "last":
                        print(even_list[- count:])

                if command[2] == "odd":
                    # If there are not enough elements to satisfy the count, print as many as you can.
                    # If there are zero even/odd elements, print an empty list "[]"
                    if count >= len(odd_list):
                        count = len(odd_list)
                    if command[0] == "first":
                        print(odd_list[:count])
                    elif command[0] == "last":
                        print(odd_list[- count:])

    command = input()

print(current_list)
