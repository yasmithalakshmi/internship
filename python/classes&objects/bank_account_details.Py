# 9. Create a class called BankAccount with account holder name and account number. Create an object and display the details.

class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number

acc = BankAccount("Ravi", 1234567890)
print("Account Holder:", acc.account_holder)
print("Account Number:", acc.account_number)
