# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of
# the product. The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.

total_price = lambda product_price, quantity: product_price * quantity

input_product = input()
input_quantity = int(input())

price = 0
if input_product == "coffee":
    price = 1.50
elif input_product == "water":
    price = 1.00
elif input_product == "coke":
    price = 1.40
elif input_product == "snacks":
    price = 2.00

total_sum = total_price(price, input_quantity)
print(f"{total_sum:.2f}")
