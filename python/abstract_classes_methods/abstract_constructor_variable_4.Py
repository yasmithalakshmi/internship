#abstract class BankAccount with account holder and account number. Add an abstract method calculate_interest().
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

    @abstractmethod
    def calculate_interest(self, amount):
        pass
class SavingsAccount(BankAccount):
    def calculate_interest(self, amount):
        interest = amount * 0.04
        print(f"Interest for Savings Account of {self.account_holder} with account number {self.account_number} on {amount} is {interest}.")
class CurrentAccount(BankAccount):
    def calculate_interest(self, amount):
        interest = amount * 0.02
        print(f"Interest for Current Account of {self.account_holder} with account number {self.account_number} on {amount} is {interest}.")
savings=SavingsAccount("yashu", "SA123")
current=CurrentAccount("yashu", "CA456")
savings.calculate_interest(10000)
current.calculate_interest(20000)
        