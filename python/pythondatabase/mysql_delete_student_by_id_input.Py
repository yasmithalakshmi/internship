# 4. Accept a student ID from the user and delete the student record.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
student_id = int(input("Enter student ID to delete: ") )
query = "DELETE FROM students WHERE id = %s"
cursor.execute(query, (student_id,))
mydb.commit()
print("Student deleted successfully.")

