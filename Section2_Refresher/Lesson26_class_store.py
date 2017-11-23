class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        # total = 0
        # for item in self.items:
        #    total += item['price']
        # return total
        return sum((item['price']) for item in self.items)


Target = Store('Target')
Target.add_item('shoes', 29.99)
Target.add_item('socks', 9.99)

print(Target.stock_price())