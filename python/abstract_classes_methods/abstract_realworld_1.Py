# abstract ATM class with methods for withdrawal, deposit, and balance checking. Implement it using a concrete bank class.
from abc import ABC, abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass
class Bank(ATM):
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
bank = Bank()
bank.deposit(1000)
bank.check_balance()
bank.withdraw(500)
bank.check_balance()