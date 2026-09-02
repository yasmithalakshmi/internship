# 2. Write a Python program to update a student's name.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

student_id = 1
new_name = "Priya"
query = "UPDATE students SET name = %s WHERE id = %s"
cursor.execute(query, (new_name, student_id))
mydb.commit()
print("Student name updated successfully.")

