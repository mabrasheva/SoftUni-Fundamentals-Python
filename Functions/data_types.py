# Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real",
# or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.

def data_type(data_type, data):
    if data_type == "int":
        return int(data) * 2
    elif data_type == "real":
        result = float(data) * 1.5
        return f"{result:.2f}"
    elif data_type == "string":
        return f"${str(data)}$"


input_type = input()
input_data_type = input()

print(data_type(input_type, input_data_type))
