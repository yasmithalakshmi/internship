# abstract class Payment with an abstract method pay(). Implement it in UPIPayment and CardPayment.
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using UPI.")
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Card.")
upi=UPIPayment()
card=CardPayment()
upi.pay(1000)
card.pay(2000)