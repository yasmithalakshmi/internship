# 3. Create employees and departments tables and retrieve employee department names using JOIN.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = '''
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
'''
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

