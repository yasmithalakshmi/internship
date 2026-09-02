# 8. Create a BankAccount class with account_holder, account_number, and balance. Create two objects.

class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

acc1 = BankAccount("Kavya", 101, 5000)
acc2 = BankAccount("Vikram", 102, 7000)

print("Account 1:", acc1.account_holder, acc1.account_number, acc1.balance)
print("Account 2:", acc2.account_holder, acc2.account_number, acc2.balance)
