# 7. Create a Number class with methods to check whether a number is even, odd, prime, or palindrome.

class Number:
    def is_even(self, n):
        return n % 2 == 0

    def is_odd(self, n):
        return n % 2 != 0

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_palindrome(self, n):
        original = n
        reverse = 0
        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n = n // 10
        return reverse == original

num = Number()
print(num.is_even(8))
print(num.is_odd(7))
print(num.is_prime(11))
print(num.is_palindrome(121))
