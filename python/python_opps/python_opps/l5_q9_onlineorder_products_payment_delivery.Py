# Level 5: Combined Relationships - Question 9
# OnlineOrder HAS-A Products and USES-A PaymentService and DeliveryService

class Product:
    def __init__(self, name):
        self.name = name


class PaymentService:
    def pay(self, amount):
        print(f"Payment processed: ${amount}")


class DeliveryService:
    def deliver(self, address):
        print(f"Delivering to: {address}")


class OnlineOrder:
    def __init__(self):
        self.products = []
        self.payment_service = PaymentService()
        self.delivery_service = DeliveryService()
    
    def add_product(self, product):
        self.products.append(product)
    
    def place_order(self, address):
        self.payment_service.pay(100)
        self.delivery_service.deliver(address)


# Example usage
order = OnlineOrder()
order.add_product(Product("Laptop"))
order.place_order("123 Main Street")
