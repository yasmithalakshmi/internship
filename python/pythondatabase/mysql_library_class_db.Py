# 8. Create a Library class with methods to issue and return books using database records.

import mysql.connector

class Library:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def issue_book(self, book_id, student_name):
        print("Book issued to", student_name)

    def return_book(self, book_id):
        print("Book returned.")

lib = Library()
lib.issue_book(1, "Asha")

