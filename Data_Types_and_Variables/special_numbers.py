# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

count = int(input())

for number in range(1, count + 1):
    total_sum = 0
    digits = number
    while digits > 0:
        total_sum += digits % 10
        digits = digits // 10
    if total_sum == 5 or total_sum == 7 or total_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
