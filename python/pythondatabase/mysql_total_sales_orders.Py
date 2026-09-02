# 5. Write a Python program to calculate the total sales from an orders table.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = "SELECT SUM(amount) FROM orders"
cursor.execute(query)
print("Total sales:", cursor.fetchone()[0])

