# 6. Display employees sorted by salary in descending order.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT * FROM employees ORDER BY salary DESC"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

