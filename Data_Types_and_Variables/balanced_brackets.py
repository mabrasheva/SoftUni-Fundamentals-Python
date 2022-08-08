# On the first line, you will receive n – the number of lines, which will follow.
# On the following n lines, you will receive one of the following:
# •	Opening bracket – "(",
# •	Closing bracket – ")" or
# •	Random string
# Your task is to find out if the brackets are balanced.
# That means after every closing bracket should follow an opening one.
# Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
# the expression should be marked as unbalanced.
# You should print "BALANCED" if the parentheses are balanced and "UNBALANCED" otherwise.

symbol_count = int(input())
message = ""
message_is_balanced = False

for line in range(symbol_count):
    symbol = input()
    if symbol == "(" or symbol == ")":
        message += symbol
# print(message)
if len(message) % 2 == 0:
    odd_positions = message[0:: 2]
    even_positions = message[1:: 2]
    if set(odd_positions) == {"("} and set(even_positions) == {")"}:
        message_is_balanced = True

if message_is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
