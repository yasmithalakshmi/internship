# 10. Create a Product class with a method to calculate the total cost based on price and quantity.

class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

p = Product(200, 5)
print("Total cost:", p.total_cost())
