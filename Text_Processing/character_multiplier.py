# Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of
# their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum, then
# continue with the next two characters. If one of the strings is longer than the other, add the remaining character
# codes to the total sum without multiplication.

def total_sum(first, second):
    result = 0
    if len(first) == len(second):
        for index in range(len(first)):
            result += ord(first[index]) * ord(second[index])
    else:
        if len(first) > len(second):
            for index in range(len(second)):
                result += ord(first[index]) * ord(second[index])
            for index in range(len(second), len(first)):
                result += ord(first[index])
        elif len(first) < len(second):
            for index in range(len(first)):
                result += ord(first[index]) * ord(second[index])
            for index in range(len(first), len(second)):
                result += ord(second[index])
    return result


first_string, second_string = input().split()
print(total_sum(first_string, second_string))
