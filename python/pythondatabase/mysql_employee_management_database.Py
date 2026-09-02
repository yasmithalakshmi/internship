# 2. Create an Employee Management Database with employees, departments, and salaries tables.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
queries = [
    "CREATE TABLE IF NOT EXISTS departments (department_id INT AUTO_INCREMENT PRIMARY KEY, department_name VARCHAR(100))",
    "CREATE TABLE IF NOT EXISTS employees (employee_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), department_id INT, salary DECIMAL(10,2))",
    "CREATE TABLE IF NOT EXISTS salaries (salary_id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, amount DECIMAL(10,2))"
]
for query in queries:
    cursor.execute(query)
print("Employee management database ready.")

