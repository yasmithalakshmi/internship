import sqlite3

# Question 7: Find students belonging to the Python course

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students WHERE course = ?", ("Python",))
students = cursor.fetchall()

print("Python Course Students:")
for student in students:
    print(student)

connection.close()
