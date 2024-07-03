class Restaurant:
    def __init__(self, name: str, logo: object, rating: float):
        self.name = name
        self.logo = logo
        self.rating = rating
        self.menu = []

    def add_item(self, item: Item):
        self.menu.append(item)

    def remove_item(self, item: Item):
        self.menu.remove(item)

    def get_menu(self):
        return self.menu