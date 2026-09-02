# Level 3: USES-A Relationship - Question 2
# Create a BankAccount class and a PaymentService class

class PaymentService:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")
        return True


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.payment_service = PaymentService()
    
    def make_payment(self, amount):
        if self.payment_service.process_payment(amount):
            self.balance -= amount
            print(f"Payment successful! New Balance: {self.balance}")


# Example usage
account = BankAccount("John", 5000)
account.make_payment(500)
