def family(years, km):
    tax = 50 + (km // 3000 * 12) - (years * 5)
    print(f"A family car will pay {tax:.2f} euros in taxes.")
    return tax


def heavy_duty(years, km):
    tax = 80 + (km // 9000 * 14) - (years * 8)
    print(f"A heavyDuty car will pay {tax:.2f} euros in taxes.")
    return tax


def sports(years, km):
    tax = 100 + (km // 2000 * 18) - (years * 9)
    print(f"A sports car will pay {tax:.2f} euros in taxes.")
    return tax


vehicles = input().split(">>")
total_tax = 0

for vehicle in vehicles:
    car_type, years_tax, kilometers = vehicle.split()
    years_tax, kilometers = int(years_tax), int(kilometers)
    car_tax = 0
    if car_type == "family":
        car_tax = family(years_tax, kilometers)
    elif car_type == "heavyDuty":
        car_tax = heavy_duty(years_tax, kilometers)
    elif car_type == "sports":
        car_tax = sports(years_tax, kilometers)
    else:
        print("Invalid car type.")
    total_tax += car_tax

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
