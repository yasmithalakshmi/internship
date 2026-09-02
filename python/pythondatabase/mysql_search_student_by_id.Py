# 6. Write a Python program to search for a student using their ID.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
student_id = 1
query = "SELECT * FROM students WHERE id = %s"
cursor.execute(query, (student_id,))
row = cursor.fetchone()
print(row)

