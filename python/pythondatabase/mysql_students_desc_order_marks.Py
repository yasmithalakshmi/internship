# 9. Write a Python program to display students in descending order of marks.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT * FROM students ORDER BY marks DESC"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

