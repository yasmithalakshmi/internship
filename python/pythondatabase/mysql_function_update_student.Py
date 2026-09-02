# 4. Create a function update_student() to update student details.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def update_student(student_id, new_name, new_course):
    cursor = mydb.cursor()
    query = "UPDATE students SET name = %s, course = %s WHERE id = %s"
    cursor.execute(query, (new_name, new_course, student_id))
    mydb.commit()
    print("Student updated.")

update_student(1, "Rita", "MCA")

