# # Read two integer numbers and, after that, exchange their values.
# # Print the variable values before and after the exchange, as shown below:
# Before:
# a = 5
# b = 10
# After:
# a = 10
# b = 5

a = int(input())
b = int(input())
a_before = a
b_before = b
a = b_before
b = a_before
print(f"""Before:
a = {a_before}
b = {b_before}
After:
a = {a}
b = {b}
""")
