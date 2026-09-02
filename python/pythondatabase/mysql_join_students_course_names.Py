# 5. Retrieve students along with their course names using JOIN.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()
query = '''
SELECT s.name, c.course_name
FROM students s
JOIN courses c ON s.course_id = c.course_id
'''
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

