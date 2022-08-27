# Write a function that receives a string and a counter n. The function should return a new string – the result of
# repeating the old string n times. Print the result of the function. Try using lambda.


result_function = lambda string, counter: string * counter

input_string = input()
input_counter = int(input())

result = result_function(input_string, input_counter)

print(result)
