# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20,
# 30...).
# Your task is to create a function that returns a loading bar depending on the number you have received in the input.
# Print the result on the console.

def loading_bar(percent_loaded):
    if percent_loaded == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    count_percent = percent_loaded // 10
    count_points = 10 - count_percent
    return f"{percent_loaded}% [{count_percent * '%'}{count_points * '.'}]\nStill loading..."


input_number = int(input())
print(loading_bar(input_number))
