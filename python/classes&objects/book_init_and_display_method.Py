# 3. Create a Book class using __init__() and a method to display book information.

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

book = Book("Python", "Guido", 450)
book.display()
