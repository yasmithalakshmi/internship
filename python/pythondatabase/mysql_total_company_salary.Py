# 10. Calculate the total salary paid by the company.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT SUM(salary) FROM employees"
cursor.execute(query)
print(cursor.fetchone()[0])

