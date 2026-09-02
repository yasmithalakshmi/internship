# 9. Retrieve students belonging to a particular course.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
course_name = "BCA"
query = "SELECT * FROM students WHERE course = %s"
cursor.execute(query, (course_name,))
rows = cursor.fetchall()

for row in rows:
    print(row)

