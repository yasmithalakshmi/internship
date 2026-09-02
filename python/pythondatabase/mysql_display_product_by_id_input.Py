# 9. Accept a product ID from the user and display product information.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
product_id = int(input("Enter product ID: ") )
query = "SELECT * FROM products WHERE id = %s"
cursor.execute(query, (product_id,))
row = cursor.fetchone()
print(row)

