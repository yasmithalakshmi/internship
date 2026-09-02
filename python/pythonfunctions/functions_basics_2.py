# 2. Function Basics - Part 2

def display_student(name, marks):
    print("Student Name:", name)
    print("Marks:", marks)


def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def smallest_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def is_palindrome_number(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return original == reverse


def count_characters(text):
    return len(text)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def total_without_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def largest_without_max(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


display_student("Riya", 92)
print("Largest number:", largest_of_three(10, 30, 20))
print("Smallest number:", smallest_of_three(10, 30, 20))
print("Factorial:", factorial(5))
print("Prime:", is_prime(13))
print("Palindrome:", is_palindrome_number(121))
print("Character count:", count_characters("Python"))
print("Vowel count:", count_vowels("Hello"))
print("Total:", total_without_sum([1, 2, 3, 4, 5]))
print("Largest without max:", largest_without_max([12, 45, 7, 89, 23]))
