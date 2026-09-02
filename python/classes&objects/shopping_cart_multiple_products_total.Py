# 8. Create a ShoppingCart class that stores multiple products and calculates the total bill.

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_bill(self):
        total = 0
        for item in self.products:
            total += item
        return total

cart = ShoppingCart()
cart.add_product(200)
cart.add_product(150)
cart.add_product(100)
print("Total bill:", cart.total_bill())
