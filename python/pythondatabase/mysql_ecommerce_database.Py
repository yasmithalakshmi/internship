# 3. Create an E-Commerce Database with customers, products, orders, and order items tables.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
queries = [
    "CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))",
    "CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), price DECIMAL(10,2), quantity INT)",
    "CREATE TABLE IF NOT EXISTS orders (order_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, total_amount DECIMAL(10,2))",
    "CREATE TABLE IF NOT EXISTS order_items (item_id INT AUTO_INCREMENT PRIMARY KEY, order_id INT, product_id INT, quantity INT)"
]
for query in queries:
    cursor.execute(query)
print("E-commerce database ready.")

