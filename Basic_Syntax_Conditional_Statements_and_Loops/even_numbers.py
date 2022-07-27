numbers_count = int(input())
odd_number = False

for numbers in range(numbers_count):
    number = int(input())

    if number % 2 == 1:
        odd_number = True
        break

if odd_number:
    print(f"{number} is odd!")
else:
    print("All numbers are even.")
