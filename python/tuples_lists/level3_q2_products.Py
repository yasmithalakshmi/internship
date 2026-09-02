# Level 3: Lists & Tuples - Question 2
# Create list of tuples with product name, price, quantity, calculate total value

products = [("Laptop", 50000, 2), ("Mouse", 500, 5), ("Keyboard", 2000, 3), ("Monitor", 15000, 1)]

print("Products list (name, price, quantity):")
print(products)

print("\nTotal value of each product:")
for name, price, quantity in products:
    total_value = price * quantity
    print(name, "-", total_value)
