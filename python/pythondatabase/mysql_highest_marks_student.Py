# 3. Write a Python program to find the highest marks.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT MAX(marks) FROM students"
cursor.execute(query)
print("Highest marks:", cursor.fetchone()[0])

