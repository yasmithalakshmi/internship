# 3. Write a Python program to update a student's marks.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

student_id = 2
new_marks = 95
query = "UPDATE students SET marks = %s WHERE id = %s"
cursor.execute(query, (new_marks, student_id))
mydb.commit()
print("Marks updated successfully.")

