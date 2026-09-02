# 7. Write a Python program to search for students using their name.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
name = "Asha"
query = "SELECT * FROM students WHERE name = %s"
cursor.execute(query, (name,))
rows = cursor.fetchall()
for row in rows:
    print(row)

