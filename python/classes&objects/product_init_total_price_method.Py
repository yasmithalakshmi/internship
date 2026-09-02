# 6. Create a Product class using __init__() and a method to calculate the total price.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

p = Product("Mouse", 500, 3)
print("Total price:", p.total_price())
