class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Warehouse:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    
    def search_item(self, name):
        search_results = []
        for item in self.items:
            if item.name == name:
                search_results.append(item)
        return search_results
    

item1 = Item("Chair", 10, 12)
item2 = Item("Table", 13, 9)
item3 = Item("iPhone 14 Pro", 30, 800)
item4 = Item("iPhone 15 Pro", 30, 900)
item5 = Item("Samsung S23 Ultra", 10, 500)

# Create a warehouse instance
warehouse = Warehouse()

warehouse.add_item(item1)
warehouse.add_item(item2)
warehouse.add_item(item3)
warehouse.add_item(item4)
warehouse.add_item(item5)


search_result = warehouse.search_item("iPhone 14")

for item in search_result:
    print("Item name: ", item.name)
    print("Price: ", item.price)
    print("Quantity: ", item.quantity)