#exception handling assert statement example
try:
    num = int(input("Enter a positive number: "))
    assert num > 0, "The number is negative."
    print("You entered a positive number:", num)
except AssertionError as e:
    print("Error:", e)
else:
    print("Assertion passed. The number is positive.")