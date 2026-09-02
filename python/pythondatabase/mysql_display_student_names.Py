# 7. Retrieve and display only student names from the database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
cursor.execute("SELECT name FROM students")
rows = cursor.fetchall()

for name in rows:
    print(name[0])

