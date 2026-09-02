# Level 10 - Question 6
# Number Analyzer for positive/negative, even/odd, and range checks.

number = int(input("Enter a number: "))
print("Positive:", number > 0)
print("Negative:", number < 0)
print("Even:", number % 2 == 0)
print("In range 10 to 50:", 10 <= number <= 50)
