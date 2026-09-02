# 1. Create a function add_student() to insert a student into the database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def add_student(name, age, course, marks):
    cursor = mydb.cursor()
    sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, age, course, marks))
    mydb.commit()
    print("Student added.")

add_student("Pooja", 22, "BCA", 87)

