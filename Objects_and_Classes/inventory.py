# Create a class Inventory.
# The __init__ method should accept only the __capacity: int (private attribute) of the inventory.
# You can read more about private attributes here.
# Each inventory should also have an attribute called items - empty list, where all the items will be stored.
# The class should also have 3 methods:
# •	add_item(item: str) - adds the item in the inventory if there is space for it. Otherwise, returns
# "not enough room in the inventory"
# •	get_capacity() - returns the value of __capacity
# •	__repr__() - returns "Items: {items}.\nCapacity left: {left_capacity}". The items should be separated by ", "

class Inventory:

    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        left_capacity = self.capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"

# Tests:
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)
