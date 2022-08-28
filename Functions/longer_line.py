# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which
# is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous
# problem. If the lines are of equal length, print only the first one. The resulting coordinates must be formatted to
# the lower integer.

from math import floor, sqrt


def closest_point(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def calculate_closest_point_of_two(x1, y1, x2, y2):
    first_distance = closest_point(x1, y1, 0, 0)
    second_distance = closest_point(0, 0, x2, y2)

    if first_distance > second_distance:
        closest_point_coordinates = tuple([floor(x2), floor(y2)])
        farthest_point_coordinates = tuple([floor(x1), floor(y1)])
    else:
        closest_point_coordinates = tuple([floor(x1), floor(y1)])
        farthest_point_coordinates = tuple([floor(x2), floor(y2)])

    return f"{closest_point_coordinates}{farthest_point_coordinates}"


def line_length(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())
x3_input = float(input())
y3_input = float(input())
x4_input = float(input())
y4_input = float(input())

first_line = [x1_input, y1_input, x2_input, y2_input]
second_line = [x3_input, y3_input, x4_input, y4_input]

first_line_distance = line_length(x1_input, y1_input, x2_input, y2_input)
second_line_distance = line_length(x3_input, y3_input, x4_input, y4_input)

if first_line_distance >= second_line_distance:
    result = calculate_closest_point_of_two(x1_input, y1_input, x2_input, y2_input)
else:
    result = calculate_closest_point_of_two(x3_input, y3_input, x4_input, y4_input)

print(result)
