# 7. Write a Python program to calculate average salary for each department.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT department, AVG(salary) FROM employees GROUP BY department"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

