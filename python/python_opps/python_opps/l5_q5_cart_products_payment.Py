# Level 5: Combined Relationships - Question 5
# ShoppingCart HAS-A Products and USES-A PaymentGateway

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentGateway:
    def pay(self, amount):
        print(f"Processing payment: ${amount}")


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.payment_gateway = PaymentGateway()
    
    def add_product(self, product):
        self.products.append(product)
    
    def checkout(self):
        total = sum(p.price for p in self.products)
        self.payment_gateway.pay(total)


# Example usage
cart = ShoppingCart()
cart.add_product(Product("Laptop", 1000))
cart.add_product(Product("Mouse", 50))
cart.checkout()
