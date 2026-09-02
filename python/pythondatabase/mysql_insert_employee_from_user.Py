# 8. Accept employee details from the user and insert them into an employees table.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
name = input("Enter employee name: ")
department = input("Enter department: ")
salary = float(input("Enter salary: ") )
joining_date = input("Enter joining date (YYYY-MM-DD): ")

query = "INSERT INTO employees (name, department, salary, joining_date) VALUES (%s, %s, %s, %s)"
values = (name, department, salary, joining_date)
cursor.execute(query, values)
mydb.commit()
print("Employee inserted successfully.")

