# Level 5: Combined Relationships - Question 4
# Library HAS-A Books and USES-A SearchService

class Book:
    def __init__(self, title):
        self.title = title


class SearchService:
    def search(self, keyword):
        print(f"Searching for: {keyword}")
        return ["Book1", "Book2"]


class Library:
    def __init__(self):
        self.books = []
        self.search_service = SearchService()
    
    def add_book(self, book):
        self.books.append(book)
    
    def find_book(self, keyword):
        results = self.search_service.search(keyword)
        print(f"Found: {results}")


# Example usage
library = Library()
library.add_book(Book("Python 101"))
library.find_book("Python")
