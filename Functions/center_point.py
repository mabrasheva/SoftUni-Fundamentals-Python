# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate
# lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the
# format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be
# formatted to the lower integer.

from math import floor


def closest_point(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


x1_input = float(input())
y1_input = float(input())
x2_input = float(input())
y2_input = float(input())

first_distance = closest_point(x1_input, y1_input, 0, 0)
second_distance = closest_point(0, 0, x2_input, y2_input)

if first_distance > second_distance:
    result = tuple([floor(x2_input), floor(y2_input)])
else:
    result = tuple([floor(x1_input), floor(y1_input)])

print(result)
