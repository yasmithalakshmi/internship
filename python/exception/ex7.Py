#exception handling with else block
print("program for division")
try:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    c = a/b
except ZeroDivisionError as e:
    print("error: division by zero is not allowed", e)
else:
    print("the result is: ", c)
print("program completed")