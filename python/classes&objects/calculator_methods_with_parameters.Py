# 1. Create a Calculator class with methods that accept parameters and return calculation results.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

c = Calculator()
print(c.add(7, 3))
print(c.subtract(7, 3))
print(c.multiply(7, 3))
print(c.divide(7, 3))
