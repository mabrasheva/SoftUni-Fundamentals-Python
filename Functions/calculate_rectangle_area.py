# Create a function that calculates and returns the area of a rectangle by given width and height.
# Print the result on the console.

area_rectangle = lambda width, height: width * height

input_width = int(input())
input_height = int(input())

result = area_rectangle(input_width, input_height)
print(result)
