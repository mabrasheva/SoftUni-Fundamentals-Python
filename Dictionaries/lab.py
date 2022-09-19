# a = dict(name="Gosho", age=15)
# print(a)

######################################

# letters = ["a", "b", "c", "d"]
# numbers_list = [1, 2, 3, 4]
# result = dict(zip(letters, numbers_list))
# print(result)

######################################

# * unzip list
# ** unzip dictionary

######################################

# scenario 1:
# data = input().split() # bread 10 butter 4 sugar 9
# product_dict = {}
# for i in range(0, len(data), 2):
#     product_dict[data[i]] = int(data[i+1])
# print(product_dict) # {'bread': 10, 'butter': 4, 'sugar': 9}

# scenario 2:
# data = input().split()
# product_dict = {data[i]:int(data[i+1]) for i in range (0, len(data),2)}
# print(product_dict)

# scenario 3:
# data = input().split()
# product_dict = {}
# for i in range(0, len(data), 2):
#     key = data[i]
#     value = data[i + 1]
#     product_dict[key] = int(value)
# print(product_dict)

######################################

# squares = {1: "one", 2: "two"}
# print("# keys:")
# for element in squares.keys():
#     print(element)
# print("# values:")
# for element in squares.values():
#     print(element)
# print("# items:")
# for element in squares.items():
#     print(element)
# print("# key value")
# for key, value in squares.items():
#     print(key, value)

######################################

# product_inventory = {}
#
# while True:
#     command = input()
#     if command == "statistics":
#         break
#
#     command = command.split(": ")
#     product = command[0]
#     quantity = int(command[1])
#
#     if product not in product_inventory:
#         product_inventory[product] = quantity
#     else:
#         product_inventory[product] += quantity
#
# print("Products in stock: ")
# product_representation = [f"- {item}: {str(product_inventory[item])}" for item in product_inventory]
# print("\n". join(product_representation))
# print(f"Total Products: {len(product_inventory)}")
# print(f"Total Quantity: {sum(product_inventory.values())}")

######################################

# numbers_1 = {1: "one", 2: "two"}
# numbers_2 = {3: "three", 4: "four"}
#
# numbers_1.update(numbers_2)
# print(numbers_1)  # {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

######################################
#
# example_dict = {"nums": {1: {"test1": "test_one", "test2": "test_two"}}}
# print(example_dict["nums"][1]["test1"])  # "test_one"
# If the key does not exist it is added to the dictionary:
# example_dict["chars"] = {"plus": "+", "minus": "-"}
# print(example_dict)  # {'nums': {1: {'test1': 'test_one', 'test2': 'test_two'}}, 'chars': {'plus': '+', 'minus': '-'}}

######################################

# example_dict = {"a": []}
# example_dict["a"].append("value")
# print(example_dict)  # {'a': ['value']}
# example_dict["a"].append("value2")
# print(example_dict)  # {'a': ['value', 'value2']}

######################################