# 1. Function Basics - Part 1

def greet():
    print("Hello, Welcome to Python!")


def welcome(name):
    print(f"Welcome {name}!")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


# Calling the functions
greet()
welcome("Alice")
print("Sum:", add(10, 5))
print("Difference:", subtract(20, 8))
print("Product:", multiply(4, 6))
