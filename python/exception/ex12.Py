#nested try in exception handling
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result of division is:", result)
except ValueError:
    print("Error: Please enter valid integers.")