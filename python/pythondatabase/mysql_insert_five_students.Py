# 5. Insert five student records into the students table using Python.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

records = [
    ("Asha", 18, "BCA", 82),
    ("Ravi", 19, "BCA", 90),
    ("Meena", 20, "BSc", 74),
    ("Kiran", 21, "MBA", 85),
    ("Anu", 22, "MCA", 92)
]

sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, records)
mydb.commit()
print("5 student records inserted successfully.")

