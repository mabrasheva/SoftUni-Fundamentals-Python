number_of_cities = int(input())
all_cities_total = 0

for number in range(1, number_of_cities + 1):
    city = input()
    earned = float(input())
    expenses = float(input())
    if number % 3 == 0 and number % 5 != 0:
        expenses *= 1.50
    if number % 5 == 0:
        earned *= 0.90
    city_total = earned - expenses
    all_cities_total += city_total
    print(f"In {city} Burger Bus earned {city_total:.2f} leva.")

print(f"Burger Bus total profit: {all_cities_total:.2f} leva.")
