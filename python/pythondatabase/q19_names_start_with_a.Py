import sqlite3

# Question 19: Search students whose names start with "A"

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("A%",))
students = cursor.fetchall()

print("Students whose names start with 'A':")
for student in students:
    print(student)

if not students:
    print("No students found.")

connection.close()
