# On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain.
# On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the
# following format:
# "{car}|{mileage}|{fuel}"
# Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is
# given:
# •	"Drive : {car} : {distance} : {fuel}":
# o	You need to drive the given distance, and you will need the given fuel to do that.
# If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
# o	If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its
# fuel with the given fuel, and print:
# "{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
# o	You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and
# print: "Time to sell the {car}!"
# •	"Refuel : {car} : {fuel}":
# o	Refill the tank of your car.
# o	Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the
# tank, take only what is required to fill it up.
# o	Print a message in the following format: "{car} refueled with {fuel} liters"
# •	"Revert : {car} : {kilometers}":
# o	Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with
# in the following format:
# "{car} mileage decreased by {amount reverted} kilometers"
# o	If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and
# DO NOT print anything.
# Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
# "{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
# Input/Constraints
# •	The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
# •	The fuel and distance amounts in the commands will never be negative.
# •	The car names in the commands will always be valid cars in your possession.

def drive(car, distance, fuel):
    distance, fuel = int(distance), int(fuel)
    if cars[car]["fuel"] < fuel:
        print("Not enough fuel to make that ride")
    else:
        cars[car]["mileage"] += distance
        cars[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")


def refuel(car, fuel):
    fuel = int(fuel)
    current_fuel = cars[car]["fuel"]
    if current_fuel + fuel > 75:
        print(f"{car} refueled with {75 - current_fuel} liters")
        cars[car]["fuel"] = 75
    else:
        cars[car]["fuel"] += fuel
        print(f"{car} refueled with {fuel} liters")


def revert(car, kilometers):
    kilometers = int(kilometers)
    cars[car]["mileage"] -= kilometers
    if cars[car]["mileage"] < 10000:
        cars[car]["mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")


number_of_cars = int(input())
cars = {}
for line in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
command = input()
while command != "Stop":
    if command.startswith("Drive"):
        action, car, distance, fuel = command.split(" : ")
        drive(car, distance, fuel)
    elif command.startswith("Refuel"):
        action, car, fuel = command.split(" : ")
        refuel(car, fuel)
    elif command.startswith("Revert"):
        action, car, kilometers = command.split(" : ")
        revert(car, kilometers)
    command = input()

for car in cars:
    print(f'{car} -> Mileage: {cars[car]["mileage"]} kms, Fuel in the tank: {cars[car]["fuel"]} lt.')
