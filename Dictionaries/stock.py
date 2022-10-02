# After you have completed your first task, your boss decides to give you another one right away.
# Now not only you have to keep track of the stock, but also you should answer customers if you have some products in
# stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".

elements_list = input().split()
search_elements = input().split()

bakery = {}

for index in range(0, len(elements_list), 2):
    key = elements_list[index]
    value = elements_list[index + 1]
    bakery[key] = int(value)
    # bakery[elements_list[index]] = int(elements_list[index + 1])

for product in search_elements:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
