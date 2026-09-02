# 5. Create a function delete_student() to delete a student.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def delete_student(student_id):
    cursor = mydb.cursor()
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    mydb.commit()
    print("Student deleted.")

delete_student(5)

