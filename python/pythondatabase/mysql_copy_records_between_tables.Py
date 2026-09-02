# 7. Write a program to copy records from one table to another.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "INSERT INTO students_backup SELECT * FROM students"
cursor.execute(query)
mydb.commit()
print("Records copied successfully.")

