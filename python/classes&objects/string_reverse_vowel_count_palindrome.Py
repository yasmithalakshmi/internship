# 8. Create a StringOperations class with methods to reverse a string, count vowels, and check palindrome.

class StringOperations:
    def reverse(self, text):
        return text[::-1]

    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for ch in text:
            if ch in vowels:
                count += 1
        return count

    def is_palindrome(self, text):
        return text == text[::-1]

s = StringOperations()
print(s.reverse("python"))
print(s.count_vowels("hello"))
print(s.is_palindrome("madam"))
