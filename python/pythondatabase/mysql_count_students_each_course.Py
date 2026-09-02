# 8. Write a Python program to count students in each course.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT course, COUNT(*) FROM students GROUP BY course"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

