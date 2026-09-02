# 5. Write a Python program to delete a student using their ID.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
student_id = 4
query = "DELETE FROM students WHERE id = %s"
cursor.execute(query, (student_id,))
mydb.commit()
print("Student deleted successfully.")

