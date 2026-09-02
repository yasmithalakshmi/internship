# 4. Write a Python program to find the lowest marks.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT MIN(marks) FROM students"
cursor.execute(query)
print("Lowest marks:", cursor.fetchone()[0])

