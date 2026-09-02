# 2. Create an Employee class that performs CRUD operations using a database.

import mysql.connector

class Employee:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def add_employee(self, name, department, salary):
        sql = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, department, salary))
        self.mydb.commit()
        print("Employee added.")

emp = Employee()
emp.add_employee("Naveen", "IT", 56000)

