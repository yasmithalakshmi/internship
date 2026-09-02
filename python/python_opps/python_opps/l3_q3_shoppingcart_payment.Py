# Level 3: USES-A Relationship - Question 3
# Create a ShoppingCart and PaymentGateway class

class PaymentGateway:
    def process_checkout(self, amount):
        print(f"Processing checkout for ${amount}")
        return True


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_gateway = PaymentGateway()
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def checkout(self):
        total = sum(price for item, price in self.items)
        if self.payment_gateway.process_checkout(total):
            print(f"Checkout complete! Total: ${total}")
            self.items = []


# Example usage
cart = ShoppingCart()
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 50)
cart.checkout()
