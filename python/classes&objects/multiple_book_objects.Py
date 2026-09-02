# 6. Create a Book class with title, author, price, and pages. Create multiple book objects.

class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

books = [
    Book("C Programming", "Dennis", 250, 300),
    Book("Java", "James", 400, 500),
    Book("Python", "Guido", 350, 430)
]

for book in books:
    print(book.title, book.author, book.price, book.pages)
