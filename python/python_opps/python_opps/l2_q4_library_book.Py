# Level 2: HAS-A Relationship - Question 4
# Create a Library class that HAS-A multiple Book objects

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def info(self):
        print(f"  Book: {self.title} by {self.author} (ISBN: {self.isbn})")


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        print(f"Library: {self.name}")
        print("Books:")
        for book in self.books:
            book.info()


# Example usage
library = Library("City Library")
library.add_book(Book("Python Basics", "John", "123456"))
library.add_book(Book("OOP Concepts", "Jane", "789012"))
library.add_book(Book("Data Science", "Bob", "345678"))
library.display_books()
