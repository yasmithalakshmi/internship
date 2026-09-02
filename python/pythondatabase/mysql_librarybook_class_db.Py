# 7. Create a LibraryBook class that stores book information in a database.

import mysql.connector

class LibraryBook:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def add_book(self, title, author):
        sql = "INSERT INTO books (title, author) VALUES (%s, %s)"
        self.cursor.execute(sql, (title, author))
        self.mydb.commit()

book = LibraryBook()
book.add_book("Python Basics", "John")
print("Book added.")

