# 6. Retrieve customers along with their orders using JOIN.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = '''
SELECT c.name, o.order_id, o.amount
FROM customers c
JOIN orders o ON c.id = o.customer_id
'''
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

