# Mini Project: Library Management System
# Demonstrates IS-A, HAS-A, and USES-A relationships

class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id


class Librarian(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        print(f"Librarian {self.name} created")


class Member(Person):
    def __init__(self, name, person_id):
        super().__init__(name, person_id)
        self.borrowed_books = []


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True


class SearchEngine:
    def search(self, books, keyword):
        results = [b for b in books if keyword.lower() in b.title.lower()]
        return results


class BorrowingService:
    def borrow_book(self, book, member):
        if book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"{member.name} borrowed {book.title}")
            return True
        else:
            print(f"{book.title} is not available")
            return False
    
    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"{member.name} returned {book.title}")
            return True
        else:
            print(f"{member.name} doesn't have {book.title}")
            return False


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
        self.members = []
        self.librarian = None
        self.search_engine = SearchEngine()
        self.borrowing_service = BorrowingService()
    
    def set_librarian(self, librarian):
        self.librarian = librarian
    
    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")
    
    def register_member(self, member):
        self.members.append(member)
        print(f"Member registered: {member.name}")
    
    def search_books(self, keyword):
        print(f"\nSearching for '{keyword}'...")
        results = self.search_engine.search(self.books, keyword)
        if results:
            print("Found books:")
            for book in results:
                status = "Available" if book.is_available else "Not Available"
                print(f"  - {book.title} by {book.author} ({status})")
        else:
            print("No books found!")
        return results
    
    def borrow_book(self, member, book):
        print(f"\n{member.name} wants to borrow {book.title}")
        self.borrowing_service.borrow_book(book, member)
    
    def return_book(self, member, book):
        print(f"\n{member.name} wants to return {book.title}")
        self.borrowing_service.return_book(book, member)
    
    def display_library_info(self):
        print(f"\n--- {self.library_name} ---")
        print(f"Librarian: {self.librarian.name if self.librarian else 'Not assigned'}")
        print(f"Total Books: {len(self.books)}")
        print(f"Total Members: {len(self.members)}")


# Example usage
if __name__ == "__main__":
    # Create library
    library = Library("City Library")
    
    # Add librarian
    librarian = Librarian("Mrs. Johnson", "L001")
    library.set_librarian(librarian)
    
    # Add books
    library.add_book(Book("Python Basics", "John Doe", "ISBN001"))
    library.add_book(Book("OOP Concepts", "Jane Smith", "ISBN002"))
    library.add_book(Book("Data Science", "Bob Wilson", "ISBN003"))
    
    # Register members
    member1 = Member("Alice", "M001")
    member2 = Member("Charlie", "M002")
    library.register_member(member1)
    library.register_member(member2)
    
    # Display info
    library.display_library_info()
    
    # Search books
    results = library.search_books("Python")
    
    # Borrow books
    if results:
        library.borrow_book(member1, results[0])
    
    # Try to borrow same book
    library.borrow_book(member2, results[0])
    
    # Return book
    library.return_book(member1, results[0])
    
    # Search and borrow again
    results = library.search_books("Data Science")
    if results:
        library.borrow_book(member2, results[0])
