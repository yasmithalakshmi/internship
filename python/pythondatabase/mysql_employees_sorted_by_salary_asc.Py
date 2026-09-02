# 5. Display employees sorted by salary in ascending order.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT * FROM employees ORDER BY salary ASC"
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

