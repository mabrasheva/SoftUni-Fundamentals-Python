# You will be given number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure,
# meaning that they do NOT consist of any of the characters: comma ",", period ".", or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"

count = int(input())

for string_number in range(count):
    string = input()

    string_is_pure = True
    for letter in string:
        if letter == "," or letter == "." or letter == "_":
            string_is_pure = False
            break

    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
