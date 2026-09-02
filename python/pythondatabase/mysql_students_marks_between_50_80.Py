# 8. Write a Python program to display students whose marks are between 50 and 80.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT * FROM students WHERE marks BETWEEN 50 AND 80"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

