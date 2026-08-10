#custom exception example
class CustomError(Exception):
    pass
balance = 1000
try:
    amount = int(input("Enter the amount to withdraw: "))
    if amount > balance:
        raise CustomError("Insufficient funds")
    else:
        balance -= amount
        print("Withdrawal successful. New balance:", balance)
except CustomError as e:
    print("Error: ", e)