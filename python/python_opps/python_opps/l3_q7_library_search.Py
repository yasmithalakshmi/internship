# Level 3: USES-A Relationship - Question 7
# Create a Library and SearchService class

class SearchService:
    def search_book(self, keyword):
        print(f"Searching for books with keyword: {keyword}")
        print("Found 5 books!")
        return ["Book1", "Book2", "Book3"]


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.search_service = SearchService()
    
    def find_book(self, keyword):
        print(f"Library: {self.library_name}")
        results = self.search_service.search_book(keyword)
        print(f"Results: {results}")


# Example usage
library = Library("City Library")
library.find_book("Python")
