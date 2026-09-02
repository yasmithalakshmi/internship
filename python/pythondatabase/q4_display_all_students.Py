import sqlite3

# Question 4: Display all students

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("All Students:")
for student in students:
    print(student)

connection.close()
