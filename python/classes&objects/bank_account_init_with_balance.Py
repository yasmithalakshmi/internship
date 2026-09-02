# 5. Create a BankAccount class using __init__() with account holder, account number, and initial balance.

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

acc = BankAccount("Rina", 987654321, 2500)
print("Account Holder:", acc.account_holder)
print("Account Number:", acc.account_number)
print("Balance:", acc.balance)
