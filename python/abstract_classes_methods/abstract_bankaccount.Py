# abstract class BankAccount with an abstract method calculate_interest(). Implement it using SavingsAccount and CurrentAccount.
from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self, amount):
        pass
class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        interest = amount * 0.04
        print(f"Interest for Savings Account on {amount} is {interest}.")
class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        interest = amount * 0.02
        print(f"Interest for Current Account on {amount} is {interest}.")
savings=SavingsAccount()
current=CurrentAccount()
savings.calculate_interest(10000)
current.calculate_interest(20000)