# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins, print "First player won".
# If the second player wins, print "Second player won". Otherwise, print "Draw!".

there_is_winner = False
winner = ""
input_list = []
for line in range(1, 3 + 1):
    row = input().split()
    if set(row) == {"1"}:  # Check row
        there_is_winner = True
        winner = "First"
    elif set(row) == {"2"}:  # Check row
        there_is_winner = True
        winner = "Second"
    input_list.append(row)
# Check diagonal
if input_list[0][0] == input_list[1][1] == input_list[2][2] == "1" or \
        input_list[0][2] == input_list[1][1] == input_list[2][0] == "1":
    there_is_winner = True
    winner = "First"
elif input_list[0][0] == input_list[1][1] == input_list[2][2] == "2" or \
        input_list[0][2] == input_list[1][1] == input_list[2][0] == "2":
    there_is_winner = True
    winner = "Second"

# Check column
column_one = input_list[0][0], input_list[1][0], input_list[2][0]
column_two = input_list[0][1], input_list[1][1], input_list[2][1]
column_three = input_list[0][2], input_list[1][2], input_list[2][2]
if set(column_one) == {"1"} or set(column_two) == {"1"} or set(column_three) == {"1"}:
    there_is_winner = True
    winner = "First"
elif set(column_one) == {"2"} or set(column_two) == {"2"} or set(column_three) == {"2"}:
    there_is_winner = True
    winner = "Second"

if there_is_winner:
    print(f"{winner} player won")
else:
    print("Draw!")
