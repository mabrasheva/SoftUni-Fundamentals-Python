# Your first task at your new job is to create a table of the stock in a bakery, and you really don't want to fail on
# your first day at work.
# You will receive a single line containing some food (keys) and quantities (values).
# They will be separated by a single space (the first element is the key, the second – the value, and so on).
# Create a dictionary with all the keys and values and print it on the console.

# Version 1:

# elements_list = input().split()
# bakery = {}
# keys = []
# values = []
# for index in range(0, len(elements_list)):
#     if index % 2 == 0:
#         keys.append(elements_list[index])
#     else:
#         values.append(int(elements_list[index]))
#
# bakery = dict(zip(keys, values))
#
# print(bakery)

# Version 2:

elements_list = input().split()
bakery = {}

for index in range(0, len(elements_list), 2):
    key = elements_list[index]
    value = elements_list[index + 1]

    bakery[key] = int(value)

print(bakery)
