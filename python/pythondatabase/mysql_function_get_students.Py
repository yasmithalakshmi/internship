# 2. Create a function get_students() to retrieve all students.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def get_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

for student in get_students():
    print(student)

