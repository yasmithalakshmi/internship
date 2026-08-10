#handling multiple exceptions in one except block
print("program for division")
try:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    c = a/b
    print("the result is: ", c)
except (ZeroDivisionError, ValueError) as e:
    print("error:", e)
print("program completed")