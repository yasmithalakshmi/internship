import sqlite3

# Question 15: Find the average marks using AVG()

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT AVG(marks) FROM students")
average = cursor.fetchone()[0]

print(f"Average marks: {average}")

connection.close()
