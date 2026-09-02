# 2. Accept a student ID from the user and display that student's details.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
student_id = int(input("Enter student ID: ") )
query = "SELECT * FROM students WHERE id = %s"
cursor.execute(query, (student_id,))
row = cursor.fetchone()
print(row)

