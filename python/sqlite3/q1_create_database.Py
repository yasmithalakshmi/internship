import sqlite3

# Question 1: Create a SQLite database named college.db

connection = sqlite3.connect("college.db")
print("Database 'college.db' created successfully!")
connection.close()
