# Level 7 - Question 8
# Use bitwise AND to check whether a number is even or odd.

number = int(input("Enter a number: "))
if number & 1 == 0:
    print("Even")
else:
    print("Odd")
