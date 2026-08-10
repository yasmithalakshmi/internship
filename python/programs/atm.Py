balance=50000
amount=int(input("Enter the amount to withdraw: "))
if amount<=balance and amount>0:
    print("Transaction successful.")
    balance=balance-amount
    print("Remaining balance:",balance)
elif amount>balance:
    print("Insufficient balance. Transaction failed.")
else:
    print("Invalid amount. Please enter a positive value.")
    