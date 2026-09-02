# Level 1: IS-A Relationship - Question 9
# Create a BankAccount class and derive SavingsAccount and CurrentAccount

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance!")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New Balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded!")


# Example usage
savings = SavingsAccount("John", 1000, 5)
current = CurrentAccount("Jane", 500, 1000)

savings.deposit(500)
savings.add_interest()
print()
current.withdraw(1200)
