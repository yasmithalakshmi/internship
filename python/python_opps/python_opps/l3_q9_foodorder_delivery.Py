# Level 3: USES-A Relationship - Question 9
# Create a FoodOrder and DeliveryService class

class DeliveryService:
    def deliver(self, address):
        print(f"Delivering to: {address}")
        print("Package delivered successfully!")


class FoodOrder:
    def __init__(self, order_id, customer_address):
        self.order_id = order_id
        self.customer_address = customer_address
        self.delivery_service = DeliveryService()
    
    def place_order(self):
        print(f"Order {self.order_id} placed!")
        self.delivery_service.deliver(self.customer_address)


# Example usage
order = FoodOrder("FOOD001", "123 Main Street")
order.place_order()
