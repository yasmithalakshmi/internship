# 6. Create a BankAccount class connected to a database for storing account details and transactions.

import mysql.connector

class BankAccount:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="college_db"
        )
        self.cursor = self.mydb.cursor()

    def add_account(self, holder_name, balance):
        sql = "INSERT INTO bank_accounts (account_holder, balance) VALUES (%s, %s)"
        self.cursor.execute(sql, (holder_name, balance))
        self.mydb.commit()

account = BankAccount()
account.add_account("Rahul", 2500)
print("Account created.")

