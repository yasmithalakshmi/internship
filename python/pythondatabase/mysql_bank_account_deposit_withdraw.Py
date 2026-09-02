# 1. Create a bank account table and perform deposit and withdrawal operations using Python.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

query = '''
CREATE TABLE IF NOT EXISTS bank_accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    account_holder VARCHAR(100),
    balance DECIMAL(10,2)
)
'''
cursor.execute(query)
print("Bank account table ready.")

