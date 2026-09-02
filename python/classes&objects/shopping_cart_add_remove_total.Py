# 9. Create a ShoppingCart class with methods to add products, remove products, and calculate the total.

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        self.items.remove(product)

    def total(self):
        return sum(self.items)

cart = ShoppingCart()
cart.add_product(100)
cart.add_product(200)
print(cart.total())
cart.remove_product(100)
print(cart.total())
