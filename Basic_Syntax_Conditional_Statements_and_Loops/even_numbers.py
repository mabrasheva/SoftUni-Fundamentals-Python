numbers_count = int(input())

for numbers in range(numbers_count):
    number = int(input())

    if number % 2 == 1:
        print(f"{number} is odd!")
        break
else:
    print("All numbers are even.")
