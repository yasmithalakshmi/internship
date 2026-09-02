# 1. Create a Student class with methods to insert, update, delete, and retrieve student records.

import mysql.connector

class Student:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def insert_student(self, name, age, course, marks):
        sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(sql, (name, age, course, marks))
        self.mydb.commit()
        print("Student inserted.")

    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

student = Student()
student.insert_student("Tina", 24, "BCA", 81)
print(student.get_students())

