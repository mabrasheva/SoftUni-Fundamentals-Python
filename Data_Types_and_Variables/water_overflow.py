# You have a water tank with a capacity of 255 liters.
# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive liters of water (integers), which you should pour into your tank.
# If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
# On the last line, print the liters in the tank.

capacity = 255
liters_count = int(input())
total_liters = 0
for count in range(liters_count):
    liters = int(input())
    if total_liters + liters > capacity:
        print("Insufficient capacity!")
    else:
        total_liters += liters
print(f"{total_liters}")
