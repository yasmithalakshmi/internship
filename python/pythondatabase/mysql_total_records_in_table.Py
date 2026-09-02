# 1. Write a Python program to calculate the total number of records in a table.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT COUNT(*) FROM students"
cursor.execute(query)
print("Total records:", cursor.fetchone()[0])

