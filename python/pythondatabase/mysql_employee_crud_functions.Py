# 6. Create an employee management program using separate functions for all CRUD operations.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def add_employee(name, department, salary):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", (name, department, salary))
    mydb.commit()

def get_employees():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM employees")
    return cursor.fetchall()

add_employee("Nisha", "HR", 45000)
for emp in get_employees():
    print(emp)

