# 1. Create a MySQL database named college_db using Python.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS college_db")
print("Database college_db created successfully.")

