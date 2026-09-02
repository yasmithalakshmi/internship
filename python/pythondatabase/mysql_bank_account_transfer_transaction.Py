# 2. Implement a money transfer between two bank accounts using a database transaction.

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
    cursor.execute("UPDATE bank_accounts SET balance = balance - 500 WHERE account_id = 1")
    cursor.execute("UPDATE bank_accounts SET balance = balance + 500 WHERE account_id = 2")
    mydb.commit()
    print("Transaction successful.")
except Error as e:
    mydb.rollback()
    print("Transaction failed:", e)

