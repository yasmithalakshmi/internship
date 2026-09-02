# 1. Create students and courses tables and establish a relationship between them.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

create_courses = '''
CREATE TABLE IF NOT EXISTS courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100)
)
'''
create_students = '''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
'''

cursor.execute(create_courses)
cursor.execute(create_students)
print("Students and courses tables created with relationship.")

