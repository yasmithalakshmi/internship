#exception handling with finally keyword
print("program for division")
try:
    a = int(input("enter the first number: "))
    b = int(input("enter the second number: "))
    c = a/b
    print("the result is: ", c)
except ZeroDivisionError as e:
    print("error: division by zero is not allowed", e)
finally:
    print("always executed")