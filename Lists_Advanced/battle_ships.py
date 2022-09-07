# You will be given a number n representing the number of rows of the field. On the following n lines, you will receive
# each field row as a string with numbers separated by a space. Each number greater than zero represents a ship with
# health equal to the number value.
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}".
# Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1.
# If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.


def attack(ships_list, squares_list):
    destroyed_count = 0
    for square in squares_list:
        attacked_ship = ships_list[square[0]][square[1]]  # ships_list[row][column]
        if attacked_ship == 0:
            continue
        else:
            ships_list[square[0]][square[1]] = attacked_ship - 1
            if ships_list[square[0]][square[1]] == 0:
                destroyed_count += 1
    return destroyed_count


rows_number = int(input())  # ex.3
ships = [input().split() for row in range(rows_number)]  # ex. [['1', '0', '0', '1'], ['2', '0', '0', '0'], ['0', '3', '0', '1']]
squares = input().split()  # ex. ['0-0', '1-0', '2-1', '2-1', '2-1', '1-1', '2-1']

# Turn all elements from str to int.
for index in range(len(squares)):
    squares[index] = squares[index].split("-")
    for coordinates in range(len(squares[index])):
        squares[index][coordinates] = int(squares[index][coordinates])  # ex. [[0, 0], [1, 0], [2, 1], [2, 1], [2, 1], [1, 1], [2, 1]]

# Turn all elements from str to int.
for row in range(len(ships)):
    for column in range(len(ships[row])):
        ships[row][column] = int(ships[row][column])  # ex. [[1, 0, 0, 1], [2, 0, 0, 0], [0, 3, 0, 1]]

print(attack(ships, squares))
