# The lottery is exciting. However, checking a million tickets for winnings only by hand is not. So, you are given the
# task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to
# see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at
# least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by
# commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	If the ticket is invalid: "invalid ticket"
# •	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# •	If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# •	It the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
# Constrains
# •	Number of tickets will be in range [0 … 100]

def length(ticket: str):
    if len(ticket) == 20:
        return True
    print("invalid ticket")
    return False


def valid_symbols(ticket: str):
    is_valid = False
    win_symbol = ""
    symbols = ['@', '#', '$', '^']
    middle = len(ticket) // 2
    left = ticket[:middle]
    right = ticket[middle::]
    count = 6
    for symbol in symbols:
        if symbol * count in left and symbol * count in right:
            is_valid = True
            win_symbol = symbol
            while symbol * (count + 1) in left and symbol * (count + 1) in right:
                count += 1
    if is_valid:
        if count == 10:
            print(f'ticket "{ticket}" - {count}{win_symbol} Jackpot!')
        else:
            print(f'ticket "{ticket}" - {count}{win_symbol}')
        return True
    print(f'ticket "{ticket}" - no match')
    return False


tickets_list = input().split(", ")
tickets_list = [ticket.strip() for ticket in tickets_list]

for ticket in tickets_list:
    if length(ticket):
        valid_symbols(ticket)
