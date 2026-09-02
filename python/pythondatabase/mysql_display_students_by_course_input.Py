# 5. Accept a course name from the user and display all students in that course.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
course_name = input("Enter course name: ")
query = "SELECT * FROM students WHERE course = %s"
cursor.execute(query, (course_name,))
rows = cursor.fetchall()
for row in rows:
    print(row)

