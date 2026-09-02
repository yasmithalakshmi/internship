# Level 2: HAS-A Relationship - Question 9
# Create a ShoppingCart class that HAS-A multiple Product objects

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total(self):
        return self.price * self.quantity
    
    def info(self):
        print(f"  Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total: {self.total()}")


class ShoppingCart:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def total_price(self):
        total = sum(p.total() for p in self.products)
        return total
    
    def display_cart(self):
        print("Shopping Cart:")
        for product in self.products:
            product.info()
        print(f"Total Price: {self.total_price()}")


# Example usage
cart = ShoppingCart()
cart.add_product(Product("Laptop", 50000, 1))
cart.add_product(Product("Mouse", 500, 2))
cart.add_product(Product("Keyboard", 2000, 1))
cart.display_cart()
