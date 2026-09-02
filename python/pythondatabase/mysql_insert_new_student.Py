# 1. Write a Python program to insert a new student into the database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

name = "Sonia"
age = 23
course = "MCA"
marks = 91

sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
values = (name, age, course, marks)
cursor.execute(sql, values)
mydb.commit()
print("Student inserted successfully.")

