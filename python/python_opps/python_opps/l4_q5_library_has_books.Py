# Level 4: Identify the Relationship - Question 5
# A Library has Books - HAS-A Relationship (Aggregation)

class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        print("Books in library:")
        for book in self.books:
            print(f"  - {book.title}")


# Example usage
library = Library()
library.add_book(Book("Python 101"))
library.add_book(Book("Java Advanced"))
library.display_books()
