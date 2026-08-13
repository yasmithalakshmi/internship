#abstract Payment class and use polymorphism to process different payment methods.
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class DebitCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing debit card payment of {amount}")

upi = UPIPayment()
credit_card = CreditCardPayment()
debit_card = DebitCardPayment()

upi.process_payment(1000)
credit_card.process_payment(2000)
debit_card.process_payment(500)