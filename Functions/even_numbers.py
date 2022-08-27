# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

def even_number(number):
    if number % 2 == 0:
        return True


input_list = input().split()
list_of_numbers = [int(i) for i in input_list]

result = list((filter(even_number, list_of_numbers)))
print(result)
