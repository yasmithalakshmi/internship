# abstract class Payment with abstract methods pay() and refund(). Implement them in UPI, CreditCard, and NetBanking.
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass
class UPI(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using UPI.")

    def refund(self, amount):
        print(f"Refunding {amount} to UPI account.")
class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

    def refund(self, amount):
        print(f"Refunding {amount} to Credit Card.")
class NetBanking(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Net Banking.")

    def refund(self, amount):
        print(f"Refunding {amount} to Net Banking account.")
upi=UPI()
credit=CreditCard()
net=NetBanking()
upi.pay(1000)
upi.refund(500)
credit.pay(2000)
credit.refund(1000)
net.pay(3000)
net.refund(1500)
