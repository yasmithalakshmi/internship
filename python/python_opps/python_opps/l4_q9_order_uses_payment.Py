# Level 4: Identify the Relationship - Question 9
# An Order uses a PaymentService - USES-A Relationship (Dependency)

class PaymentService:
    def pay(self, amount):
        print(f"Payment of ${amount} processed")


class Order:
    def __init__(self, order_id, payment_service):
        self.order_id = order_id
        self.payment_service = payment_service
    
    def place_order(self, amount):
        print(f"Order {self.order_id} placed")
        self.payment_service.pay(amount)


# Example usage
service = PaymentService()
order = Order("ORD001", service)
order.place_order(1000)
