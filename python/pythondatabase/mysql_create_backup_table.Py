# 6. Create a database backup table using Python.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "CREATE TABLE IF NOT EXISTS students_backup LIKE students"
cursor.execute(query)
print("Backup table created.")

