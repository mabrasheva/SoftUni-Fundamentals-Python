# You will be given two strings.
# Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

first_string = input()
second_string = input()
new_string = first_string
last_string = first_string

for letter in range(len(first_string)):
    left_side = second_string[:letter + 1]
    # print(left_side)
    right_side = first_string[letter + 1:]
    # print(right_side)
    new_string = left_side + right_side
    if new_string != last_string:
        print(new_string)
        last_string = new_string
