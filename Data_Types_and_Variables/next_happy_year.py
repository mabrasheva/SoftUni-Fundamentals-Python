# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example, 2018.
# Write a program that receives an integer number and finds the next happy year.

year = int(input())

while True:
    next_year = year + 1
    next_year_is_happy = False
    list_next_year = list(str(next_year))
    set_next_year = set(str(next_year))
    if len(list_next_year) == len(set_next_year):
        next_year_is_happy = True
    if next_year_is_happy:
        print(next_year)
        break
    year += 1
