# 3. Display employees whose salary is greater than ₹50,000.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT * FROM employees WHERE salary > 50000"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

