# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers.
# Each number represents the time needed for the car to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side.
# The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer
# with less time). If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his
# current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

time_list = input().split()
total_time_left_racer = 0
total_time_right_racer = 0
time_list = [int(time) for time in time_list]
middle = len(time_list) // 2  # The middle index of the sequence is the finish line.
left_racer_time_list = time_list[:middle]
right_racer_time_list = time_list[middle + 1:]
winner = ""
winner_time = 0

if 0 not in left_racer_time_list:
    total_time_left_racer = sum(left_racer_time_list)
else:
    for time in left_racer_time_list:
        if time != 0:
            total_time_left_racer += time
        else:
            total_time_left_racer -= 0.20 * total_time_left_racer

if 0 not in right_racer_time_list:
    total_time_right_racer = sum(right_racer_time_list)
else:
    for index in range(len(right_racer_time_list) - 1, -1, -1):
        if right_racer_time_list[index] != 0:
            total_time_right_racer += right_racer_time_list[index]
        else:
            total_time_right_racer -= 0.20 * total_time_right_racer

if total_time_left_racer > total_time_right_racer:
    winner = "right"
    winner_time = total_time_right_racer
else:
    winner = "left"
    winner_time = total_time_left_racer
print(f"The winner is {winner} with total time: {winner_time:.1f}")
