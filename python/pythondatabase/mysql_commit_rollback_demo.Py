# 3. Demonstrate commit() and rollback() using a Python database program.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
try:
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES ('Test', 20, 'BCA', 70)")
    mydb.commit()
    print("Commit successful.")
except Exception as e:
    mydb.rollback()
    print("Rollback done:", e)

