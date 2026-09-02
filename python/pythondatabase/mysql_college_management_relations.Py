# 4. Create students, courses, and enrollments tables for a college management system.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

queries = [
    "CREATE TABLE IF NOT EXISTS courses (course_id INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(100))",
    "CREATE TABLE IF NOT EXISTS students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), course_id INT)",
    "CREATE TABLE IF NOT EXISTS enrollments (enrollment_id INT AUTO_INCREMENT PRIMARY KEY, student_id INT, course_id INT)"
]
for query in queries:
    cursor.execute(query)
print("College management tables created.")

