# Level 6 - Question 10
# Demonstrate identity comparison using custom class objects.

class Book:
    pass

book1 = Book()
book2 = book1
print(book1 is book2)
