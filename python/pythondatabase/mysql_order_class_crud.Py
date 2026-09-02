# 5. Create an Order class that stores and retrieves order information.

import mysql.connector

class Order:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def add_order(self, customer_id, total_amount):
        sql = "INSERT INTO orders (customer_id, total_amount) VALUES (%s, %s)"
        self.cursor.execute(sql, (customer_id, total_amount))
        self.mydb.commit()

order = Order()
order.add_order(1, 2500)
print("Order added.")

