# Level 10 - Question 3
# Shopping Discount Calculator using arithmetic, comparison, and logical operators.

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
member = input("Are you a member? (yes/no): ")

total = price * quantity
if member.lower() == "yes":
    total = total - (total * 10 / 100)

print("Total bill:", total)
