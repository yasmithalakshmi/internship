# 6. Create a BankAccount class that prevents withdrawal when the balance is insufficient.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawal successful")

acc = BankAccount(500)
acc.withdraw(700)
