# 3. Create a function search_student() to search students by ID or name.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def search_student(value):
    cursor = mydb.cursor()
    query = "SELECT * FROM students WHERE id = %s OR name = %s"
    cursor.execute(query, (value, value))
    return cursor.fetchall()

print(search_student(1))

