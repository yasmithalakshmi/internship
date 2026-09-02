# 8. Retrieve students whose marks are greater than 75.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

query = "SELECT * FROM students WHERE marks > 75"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

