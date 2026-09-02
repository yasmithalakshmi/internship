# Function practice group 2

def display_student(name, marks):
    print("Student name:", name)
    print("Marks:", marks)


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c


def smallest_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    return c


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def is_palindrome(number):
    original = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    return original == reverse


def char_count(text):
    return len(text)


def vowel_count(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def total_without_sum(numbers):
    total = 0
    for value in numbers:
        total += value
    return total


def largest_without_max(numbers):
    largest = numbers[0]
    for value in numbers[1:]:
        if value > largest:
            largest = value
    return largest


display_student("Anu", 95)
print("Largest:", largest_of_three(40, 15, 28))
print("Smallest:", smallest_of_three(40, 15, 28))
print("Factorial:", factorial(5))
print("Prime:", is_prime(17))
print("Palindrome:", is_palindrome(121))
print("Characters:", char_count("Python"))
print("Vowels:", vowel_count("Hello World"))
print("Total:", total_without_sum([1, 2, 3, 4, 5]))
print("Largest value:", largest_without_max([10, 47, 8, 93, 21]))
