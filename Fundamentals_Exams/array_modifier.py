"""
You are given an array with integers. Write a program to modify the elements after receiving the following commands:
•	"swap {index1} {index2}" takes two elements and swap their places.
•	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index. Save the
product at the 1st index.
•	"decrease" decreases all elements in the array with 1.
Input
On the first input line, you will be given the initial array values separated by a single space.
On the next lines you will receive commands until you receive the command "end". The commands are as follow:
•	"swap {index1} {index2}"
•	"multiply {index1} {index2}"
•	"decrease"
Output
The output should be printed on the console and consist of elements of the modified array – separated by a comma and a
single space ", ".
Constraints
•	Elements of the array will be integer numbers in the range [-231...231]
•	Count of the array elements will be in the range [2...100]
•	Indexes will be always in the range of the array
"""

array_string = input().split()
array = list(map(int, array_string))
result = array

command = input()

while command != "end":

    command = command.split()
    action = command[0]

    if action == "swap":
        index_one = int(command[1])
        index_two = int(command[2])
        result[index_one], result[index_two] = result[index_two], result[index_one]

    elif action == "multiply":
        index_one = int(command[1])
        index_two = int(command[2])
        result[index_one] *= result[index_two]

    elif action == "decrease":
        result = [number - 1 for number in result]

    command = input()

print(*result, sep=", ")
