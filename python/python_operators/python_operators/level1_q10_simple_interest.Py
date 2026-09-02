# Level 1 - Question 10
# Calculate simple interest using arithmetic operators.

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
interest = (principal * rate * time) / 100
print("Simple interest:", interest)
