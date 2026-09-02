# 8. Write a program to delete multiple records based on a condition.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "DELETE FROM students WHERE marks < 40"
cursor.execute(query)
mydb.commit()
print("Records deleted successfully.")

