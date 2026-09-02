# 5. Create a Product class with a method that accepts quantity and returns the total price.

class Product:
    def total_price(self, price, quantity):
        return price * quantity

p = Product()
print(p.total_price(200, 4))
