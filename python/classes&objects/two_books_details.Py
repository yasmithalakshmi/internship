# 5. Create a class called Book with properties for title, author, and price. Create two objects and display their details.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Basics", "John", 350)
book2 = Book("Data Structures", "Alice", 500)

print("Book 1:", book1.title, book1.author, book1.price)
print("Book 2:", book2.title, book2.author, book2.price)
