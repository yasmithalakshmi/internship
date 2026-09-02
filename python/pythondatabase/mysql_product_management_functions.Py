# 7. Create a product management program using functions and a database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def add_product(name, price, quantity):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
    mydb.commit()

add_product("Laptop", 45000, 4)
print("Product added.")

