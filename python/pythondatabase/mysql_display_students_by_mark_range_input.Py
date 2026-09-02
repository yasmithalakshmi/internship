# 6. Accept minimum and maximum marks from the user and display matching students.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
min_marks = int(input("Enter minimum marks: ") )
max_marks = int(input("Enter maximum marks: ") )
query = "SELECT * FROM students WHERE marks BETWEEN %s AND %s"
cursor.execute(query, (min_marks, max_marks))
rows = cursor.fetchall()
for row in rows:
    print(row)

