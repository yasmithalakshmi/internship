# Level 4: Identify the Relationship - Question 6
# A ShoppingCart uses a PaymentGateway - USES-A Relationship (Dependency)

class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment: ${amount}")


class ShoppingCart:
    def __init__(self, payment_gateway):
        self.items = []
        self.payment_gateway = payment_gateway
    
    def add_item(self, item):
        self.items.append(item)
    
    def checkout(self):
        total = len(self.items) * 100
        self.payment_gateway.process_payment(total)


# Example usage
gateway = PaymentGateway()
cart = ShoppingCart(gateway)
cart.add_item("Laptop")
cart.checkout()
