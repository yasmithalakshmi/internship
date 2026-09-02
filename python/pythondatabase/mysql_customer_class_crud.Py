# 4. Create a Customer class with database operations.

import mysql.connector

class Customer:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def add_customer(self, name, email):
        sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, email))
        self.mydb.commit()

customer = Customer()
customer.add_customer("Aman", "aman@gmail.com")
print("Customer added.")

