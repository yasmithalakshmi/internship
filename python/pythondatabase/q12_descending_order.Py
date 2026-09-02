import sqlite3

# Question 12: Display students in descending order of marks

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students ORDER BY marks DESC")
students = cursor.fetchall()

print("Students in descending order of marks:")
for student in students:
    print(student)

connection.close()
