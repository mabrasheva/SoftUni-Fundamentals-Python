# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a
# given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def sum_odd_and_even(number):
    digits_number = str(number)
    # for digit in digits_number:
    #     list_digits_number.append(digit)
    list_digits_number = [i for i in digits_number]

    even_sum = 0
    odd_sum = 0
    for digit in list_digits_number:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


input_number = int(input())

print(sum_odd_and_even(input_number))
