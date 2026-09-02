# 2. Insert 10 employee records into the employees table using Python.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

records = [
    ("Rahul", "IT", 52000, "2021-01-10"),
    ("Priya", "HR", 48000, "2020-05-15"),
    ("Karan", "IT", 61000, "2022-07-11"),
    ("Sunita", "Finance", 55000, "2021-09-20"),
    ("Javed", "Sales", 43000, "2023-02-15"),
    ("Aditi", "IT", 67000, "2021-11-13"),
    ("Ramesh", "Support", 50000, "2019-04-21"),
    ("Neha", "Marketing", 39000, "2022-08-22"),
    ("Vikram", "IT", 71000, "2020-12-09"),
    ("Maya", "HR", 47000, "2021-06-18")
]

query = "INSERT INTO employees (name, department, salary, joining_date) VALUES (%s, %s, %s, %s)"
cursor.executemany(query, records)
mydb.commit()
print("10 employee records inserted successfully.")

