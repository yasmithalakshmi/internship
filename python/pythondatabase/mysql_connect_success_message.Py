# 3. Connect Python to a MySQL database and display a successful connection message.

import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="college_db"
    )
    print("Connected to MySQL database successfully!")
except mysql.connector.Error as e:
    print("Connection failed:", e)

