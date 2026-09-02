# 4. Create a Banking Database with customers, accounts, transactions, and branches tables.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
queries = [
    "CREATE TABLE IF NOT EXISTS customers (customer_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))",
    "CREATE TABLE IF NOT EXISTS accounts (account_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, balance DECIMAL(10,2))",
    "CREATE TABLE IF NOT EXISTS transactions (transaction_id INT AUTO_INCREMENT PRIMARY KEY, account_id INT, amount DECIMAL(10,2), type VARCHAR(20))",
    "CREATE TABLE IF NOT EXISTS branches (branch_id INT AUTO_INCREMENT PRIMARY KEY, branch_name VARCHAR(100))"
]
for query in queries:
    cursor.execute(query)
print("Banking database ready.")

