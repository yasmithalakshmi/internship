#exception handling with raise statement
print("program for division")
try:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    if b == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    c = a/b
    print("the result is: ", c)
except ZeroDivisionError as e:
    print("error:", e)