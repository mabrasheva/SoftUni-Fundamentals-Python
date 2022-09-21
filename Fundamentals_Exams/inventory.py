# Input / Constraints
# You will receive a journal with some collecting items, separated with a comma and a space (", ").
# After that, until receiving "Craft!" you will be receiving different commands split by " - ":
# •	"Collect - {item}" - you should add the given item to your inventory.
# If the item already exists, you should skip this line.
# •	"Drop - {item}" - you should remove the item from your inventory if it exists.
# •	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists.
# If so, add the new item after the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", ".

inventory = input().split(", ")
command = input()
while command != "Craft!":
    command = command.split(" - ")
    action = command[0]
    item = command[1]

    if action == "Collect":
        if item not in inventory:
            inventory.append(item)

    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)

    elif action == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert((old_item_index + 1), new_item)

    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))
