# On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30
# days). On the fourth line, you will receive the guinea pig's weight.
# Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of
# hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its
# weight.
# Calculate whether the quantity of food, hay, and cover, will be enough for a month.
# If Merry runs out of food, hay, or cover, stop the program!
# Input
# •	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
# •	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
# Output
# •	If the food, the hay, and the cover are enough, print:
# o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
# •	If one of the things is not enough, print:
# o	"Merry must go to the pet store!"
# The output values must be formatted to the second decimal place!

def run_out(product):
    run_out = False
    if product <= 0:
        run_out = True
    return run_out


food_grams = float(input()) * 1000
hay_grams = float(input()) * 1000
cover_grams = float(input()) * 1000
weight_grams = float(input()) * 1000
run_out_of_product = False

for day in range(1, 30 + 1):
    food_grams -= 300
    if run_out(food_grams):
        run_out_of_product = True
        break
    if day % 2 == 0:
        hay_grams -= 0.05 * food_grams
        if run_out(hay_grams):
            run_out_of_product = True
            break
    if day % 3 == 0:
        cover_grams -= weight_grams / 3
        if run_out(cover_grams):
            run_out_of_product = True
            break

if run_out_of_product:
    print("Merry must go to the pet store!")
else:
    print(
        f"Everything is fine! Puppy is happy! Food: {(food_grams / 1000):.2f}, Hay: {(hay_grams / 1000):.2f}, Cover: {(cover_grams / 1000):.2f}.")
