balance = 10000
amount = float(input("Enter withdrawal amount: "))
try:
    pin = int(input("Enter your PIN: "))
    if pin != 1234:
       raise ValueError("Incorrect PIN.")
    if amount <= 0:
       raise ValueError("Amount must be greater than zero.")
    if amount > balance:
       raise ValueError("Insufficient account balance.")
except ValueError as e:
    print("error", e)
else:
    
    balance-=amount
    print("amount withdrawal completed")
    
