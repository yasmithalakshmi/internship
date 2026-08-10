#exception handling with function example
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("The result is:", result)
    finally:
        print("Execution completed.")
divide(10, 2)
divide(10, 0)