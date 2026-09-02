# 8. Create a customer management program using functions and a database.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

def add_customer(name, email):
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", (name, email))
    mydb.commit()

add_customer("Riya", "riya@gmail.com")
print("Customer added.")

