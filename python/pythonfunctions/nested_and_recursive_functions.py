# 5. Nested Functions and Recursion

# 1. Function inside another function

def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()


# 2. Function that returns another function

def create_multiplier(factor):
    def multiply(value):
        return value * factor
    return multiply


# 3. Recursive factorial

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# 4. Recursive Fibonacci

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 5. Recursive sum from 1 to n

def sum_upto_n(n):
    if n == 1:
        return 1
    return n + sum_upto_n(n - 1)


outer_function()
multiplier = create_multiplier(5)
print("Multiplier:", multiplier(7))
print("Factorial:", factorial_recursive(5))
print("Fibonacci:", fibonacci(7))
print("Sum 1 to n:", sum_upto_n(5))
