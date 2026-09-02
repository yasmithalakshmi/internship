# 1. Accept student details from the user and insert them into the database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

name = input("Enter student name: ")
age = int(input("Enter age: ") )
course = input("Enter course: ")
marks = int(input("Enter marks: ") )

sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
values = (name, age, course, marks)
cursor.execute(sql, values)
mydb.commit()
print("Student inserted successfully.")

