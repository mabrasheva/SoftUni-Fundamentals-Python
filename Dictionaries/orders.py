# Write a program that keeps the information about products and their prices.
# Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is
# different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep
# adding items. Finally, print all items with their names and the total price of each product.
# Input
# •	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
# •	The product data is always delimited by a single space.
# Output
# •	Print information about each product in the following format:
# "{product_name} -> {total_price}"
# •	Format the total price to the 2nd digit after the decimal separator.

def calc_price(input_name: str, input_price: float, input_quantity: int, input_products: dict):
    if input_name not in input_products:
        input_products[input_name] = [input_quantity, input_price]
    else:
        input_products[input_name][0] += input_quantity
        input_products[input_name][1] = input_price

    return input_products


products = {}
command = input()

while command != "buy":
    name, price, quantity = command.split()
    products = calc_price(name, float(price), int(quantity), products)

    command = input()

for product, total_price in products.items():
    print(f"{product} -> {(total_price[0] * total_price[1]):.2f}")
