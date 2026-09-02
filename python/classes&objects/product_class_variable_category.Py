# 5. Create a Product class with a class variable category. Create different product objects.

class Product:
    category = "Electronics"

    def __init__(self, name):
        self.name = name

p1 = Product("Mobile")
p2 = Product("Laptop")

print(p1.name, Product.category)
print(p2.name, Product.category)
