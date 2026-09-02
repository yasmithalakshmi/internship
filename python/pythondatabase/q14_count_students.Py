import sqlite3

# Question 14: Find the total number of students using COUNT()

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
total = cursor.fetchone()[0]

print(f"Total number of students: {total}")

connection.close()
