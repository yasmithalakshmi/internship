# 8. Create a class called Product with product name, price, and quantity. Create an object and display its information.

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

p = Product("Laptop", 50000, 2)
print("Product Name:", p.product_name)
print("Price:", p.price)
print("Quantity:", p.quantity)
