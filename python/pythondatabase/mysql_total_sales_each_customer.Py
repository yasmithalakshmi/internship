# 6. Write a Python program to calculate total sales for each customer.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT customer_id, SUM(amount) FROM orders GROUP BY customer_id"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

