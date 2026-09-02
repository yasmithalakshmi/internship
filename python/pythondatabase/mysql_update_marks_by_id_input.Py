# 3. Accept a student ID and new marks from the user and update the database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
student_id = int(input("Enter student ID: ") )
new_marks = int(input("Enter new marks: ") )
query = "UPDATE students SET marks = %s WHERE id = %s"
cursor.execute(query, (new_marks, student_id))
mydb.commit()
print("Marks updated successfully.")

