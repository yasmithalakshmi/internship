# 3. Create a Product class with name, price, and quantity. Calculate the total price for each object.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

p1 = Product("Pen", 20, 5)
p2 = Product("Book", 150, 3)

print("Total price of Pen:", p1.total_price())
print("Total price of Book:", p2.total_price())
