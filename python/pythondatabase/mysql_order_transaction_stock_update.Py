# 4. Create an order system and use transactions while creating an order and updating product stock.

import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

try:
    cursor = mydb.cursor()
    mydb.start_transaction()
    cursor.execute("INSERT INTO orders (customer_id, total_amount) VALUES (1, 2500)")
    cursor.execute("UPDATE products SET quantity = quantity - 1 WHERE id = 10")
    mydb.commit()
    print("Order placed and stock updated.")
except Error as e:
    mydb.rollback()
    print("Transaction failed:", e)

