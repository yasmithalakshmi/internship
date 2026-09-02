# 2. Create a table named students with columns id, name, age, course, and marks.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

query = '''
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100),
    marks INT
)
'''

cursor.execute(query)
print("Table students created successfully.")

