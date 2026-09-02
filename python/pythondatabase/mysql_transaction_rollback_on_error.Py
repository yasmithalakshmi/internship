# 5. Write a program that rolls back a transaction when an error occurs.

import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

try:
    cursor = mydb.cursor()
    mydb.start_transaction()
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES ('Bad', 20, 'BCA', 100)")
    raise ValueError("Sample error")
except Exception as e:
    mydb.rollback()
    print("Rollback because of error:", e)

