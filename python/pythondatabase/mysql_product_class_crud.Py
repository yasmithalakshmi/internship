# 3. Create a Product class with methods for adding, updating, deleting, and searching products.

import mysql.connector

class Product:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def add_product(self, name, price, quantity):
        sql = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, price, quantity))
        self.mydb.commit()

product = Product()
product.add_product("Mouse", 700, 10)
print("Product added.")

