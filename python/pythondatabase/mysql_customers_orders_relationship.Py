# 2. Create customers and orders tables and establish a relationship using foreign keys.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

query1 = '''CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))'''
query2 = '''CREATE TABLE IF NOT EXISTS orders (order_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, amount DECIMAL(10,2), FOREIGN KEY (customer_id) REFERENCES customers(id))'''

cursor.execute(query1)
cursor.execute(query2)
print("Customer-order relationship created.")

