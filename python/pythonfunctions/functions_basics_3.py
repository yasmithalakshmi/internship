# 3. Function Basics - Part 3

def arithmetic(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b
    return add, subtract, multiply, divide


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


def average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result


def odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(num)
    return result


def reverse_string(text):
    return text[::-1]


def is_palindrome_string(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def remove_duplicates(values):
    unique = []
    for item in values:
        if item not in unique:
            unique.append(item)
    return unique


def second_largest(numbers):
    largest = max(numbers[0], numbers[1])
    second = min(numbers[0], numbers[1])

    for num in numbers[2:]:
        if num > largest:
            second = largest
            largest = num
        elif num > second:
            second = num
    return second


print(arithmetic(10, 5))
print("Grade:", grade(85))
print("Average:", average([10, 20, 30, 40]))
print("Even numbers:", even_numbers([1, 2, 3, 4, 5, 6]))
print("Odd numbers:", odd_numbers([1, 2, 3, 4, 5, 6]))
print("Reverse:", reverse_string("python"))
print("Palindrome:", is_palindrome_string("madam"))
print("Without duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print("Second largest:", second_largest([10, 20, 30, 40, 50]))
