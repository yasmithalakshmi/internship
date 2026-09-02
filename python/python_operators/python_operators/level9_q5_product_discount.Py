# Level 9 - Question 5
# Calculate a product's price after applying a discount.

price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percentage: "))
final_price = price - (price * discount_percent / 100)
print("Final price:", final_price)
