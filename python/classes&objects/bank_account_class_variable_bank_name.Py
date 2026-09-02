# 4. Create a BankAccount class with a class variable bank_name. Create multiple accounts.

class BankAccount:
    bank_name = "SBI"

    def __init__(self, account_holder):
        self.account_holder = account_holder

acc1 = BankAccount("Asha")
acc2 = BankAccount("Vikram")

print(acc1.account_holder, BankAccount.bank_name)
print(acc2.account_holder, BankAccount.bank_name)
