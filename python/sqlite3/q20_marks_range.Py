import sqlite3

# Question 20: Search students whose marks are between 60 and 90

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students WHERE marks BETWEEN ? AND ?", (60, 90))
students = cursor.fetchall()

print("Students with marks between 60 and 90:")
for student in students:
    print(student)

connection.close()
