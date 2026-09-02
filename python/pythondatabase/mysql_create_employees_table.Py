# 1. Create a table employees with employee ID, name, department, salary, and joining date.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

query = '''
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10,2),
    joining_date DATE
)
'''

cursor.execute(query)
print("Table employees created successfully.")

