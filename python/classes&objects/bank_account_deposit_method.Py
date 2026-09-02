# 4. Create a BankAccount class with a method that accepts an amount and deposits it into the account.

class BankAccount:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        return self.balance

acc = BankAccount()
print(acc.deposit(500))
