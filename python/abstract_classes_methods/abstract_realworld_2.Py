#abstract ECommercePayment class and implement UPI, Credit Card, Debit Card, and Net Banking payments.
from abc import ABC, abstractmethod
class ECommercePayment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(ECommercePayment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI.")
class CreditCard(ECommercePayment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")
class DebitCard(ECommercePayment):
    def pay(self, amount):
        print(f"Paid {amount} using Debit Card.")
class NetBanking(ECommercePayment):
    def pay(self, amount):
        print(f"Paid {amount} using Net Banking.")
upi=UPI()
upi.pay(1000)
credit=CreditCard()
credit.pay(1000)
debit=DebitCard()
debit.pay(1000)
netbanking=NetBanking()
netbanking.pay(1000)