# 4. Display employees belonging to the IT department.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT * FROM employees WHERE department = 'IT'"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

