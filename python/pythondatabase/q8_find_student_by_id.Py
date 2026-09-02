import sqlite3

# Question 8: Find the student with a particular ID

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

student_id = int(input("Enter student ID: "))

cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
student = cursor.fetchone()

if student:
    print("Student found:")
    print(student)
else:
    print("Student not found!")

connection.close()
