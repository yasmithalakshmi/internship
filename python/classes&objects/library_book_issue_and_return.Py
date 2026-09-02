# 7. Create a LibraryBook class with methods to issue and return a book.

class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.issued = False

    def issue(self):
        if not self.issued:
            self.issued = True
            print(self.title, "issued")
        else:
            print(self.title, "already issued")

    def return_book(self):
        if self.issued:
            self.issued = False
            print(self.title, "returned")
        else:
            print(self.title, "not issued")

book = LibraryBook("Python Basics")
book.issue()
book.return_book()
