# Level 3: USES-A Relationship - Question 6
# Create an Order and EmailService class

class EmailService:
    def send_email(self, recipient, subject, body):
        print(f"Email sent to: {recipient}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")


class Order:
    def __init__(self, order_id, customer_email):
        self.order_id = order_id
        self.customer_email = customer_email
        self.email_service = EmailService()
    
    def send_confirmation(self):
        subject = f"Order Confirmation - {self.order_id}"
        body = f"Your order {self.order_id} has been confirmed!"
        self.email_service.send_email(self.customer_email, subject, body)


# Example usage
order = Order("ORD001", "customer@example.com")
order.send_confirmation()
