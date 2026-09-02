# Function practice group 5

def outer_function():
    print("This is outer function.")

    def inner_function():
        print("This is inner function.")

    inner_function()


def create_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_upto_n(n):
    if n == 1:
        return 1
    return n + sum_upto_n(n - 1)


outer_function()
multiplier = create_multiplier(4)
print("Multiple:", multiplier(6))
print("Factorial:", factorial_recursive(5))
print("Fibonacci:", fibonacci(7))
print("Sum 1 to n:", sum_upto_n(5))
