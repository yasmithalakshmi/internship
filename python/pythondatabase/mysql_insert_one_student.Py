# 4. Insert one student record into the students table using Python.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
values = ("Alice", 20, "BCA", 88)

cursor.execute(sql, values)
mydb.commit()
print("1 student record inserted successfully.")

