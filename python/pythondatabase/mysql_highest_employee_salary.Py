# 7. Find the highest employee salary.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT MAX(salary) FROM employees"
cursor.execute(query)
print(cursor.fetchone()[0])

