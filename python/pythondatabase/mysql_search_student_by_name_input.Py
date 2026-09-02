# 7. Accept a student name from the user and search for the student.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
name = input("Enter student name: ")
query = "SELECT * FROM students WHERE name = %s"
cursor.execute(query, (name,))
rows = cursor.fetchall()
for row in rows:
    print(row)

