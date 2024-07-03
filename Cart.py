class Cart:
    def __init__(self):
        self.items = {}
        self.num_of_items = 0
        self.total_price = 0.0

    def number_of_items(self):
        return self.num_of_items

    def get_total_price(self):
        return self.total_price

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity
        
        self.num_of_items += quantity
        self.total_price += item.price * quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
                self.num_of_items -= quantity
                self.total_price -= self.items[item_name]['item'].price * quantity
            elif self.items[item_name]['quantity'] == quantity:
                self.num_of_items -= quantity
                self.total_price -= self.items[item_name]['item'].price * quantity
                del self.items[item_name]

    def display_cart(self):
        total = 0
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your cart:")
            for item_name, details in self.items.items():
                item = details['item']
                quantity = details['quantity']
                print(f"Item: {item.name}, Quantity: {quantity}, Total Price: ${item.price * quantity:.2f}, Calorie: {item.calorie}")
            