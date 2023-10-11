# Define a class 'Item' to represent items with name, quantity, and price.
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

# Define a class 'Warehouse' to represent a warehouse that stores items.
class Warehouse:
    def __init__(self):
        self.items = []  # Initialize a list to store items in the warehouse.
    
    def add_item(self, item):
        self.items.append(item)  # Add an item to the list of items.
    
    def remove_item(self, item):
        self.items.remove(item)  # Remove an item from the list of items.
    
    def search_item(self, name):
        for item in self.items:
            if item.name == name:
                return item  # Return the first item with a matching name.
        return "Item not found"  # Return a custom message if no matching item is found.



# Create instances of 'Item' to represent different items.
item1 = Item("Chair", 10, 12)
item2 = Item("Table", 13, 9)
item3 = Item("iPhone 14 Pro", 30, 800)
item4 = Item("iPhone 15 Pro", 30, 900)
item5 = Item("Samsung S23 Ultra", 10, 500)




# Create a 'Warehouse' instance to store items.
warehouse = Warehouse()

# Add items to the warehouse.
warehouse.add_item(item1)
warehouse.add_item(item2)
warehouse.add_item(item3)
warehouse.add_item(item4)
warehouse.add_item(item5)


# Search for items with the name "iPhone 14".
search_result = warehouse.search_item("iPhone 14")
print(search_result)
