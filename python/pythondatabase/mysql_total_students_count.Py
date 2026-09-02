# 10. Display the total number of students stored in the database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]
print("Total students:", count)

