number = int(input())

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print("*", end="")
    print()

for row in range(number - 1, 0, -1):
    for column in range(1, row + 1):
        print("*", end="")
    print()
