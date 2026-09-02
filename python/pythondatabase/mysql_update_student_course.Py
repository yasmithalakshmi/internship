# 4. Write a Python program to update a student's course.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

student_id = 3
new_course = "BSc"
query = "UPDATE students SET course = %s WHERE id = %s"
cursor.execute(query, (new_course, student_id))
mydb.commit()
print("Course updated successfully.")

