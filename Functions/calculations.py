# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", "subtract".


def calculator(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


input_operator = input()
input_a = int(input())
input_b = int(input())

print(calculator(input_a, input_b, input_operator))
