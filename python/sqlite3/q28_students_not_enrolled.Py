import sqlite3

# Question 28: Find students who are not enrolled in any course

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# LEFT JOIN to find students not in enrollments
cursor.execute("""
    SELECT students.id, students.name
    FROM students
    LEFT JOIN enrollments ON students.id = enrollments.student_id
    WHERE enrollments.student_id IS NULL
""")

results = cursor.fetchall()

print("Students not enrolled in any course:")
for student_id, student_name in results:
    print(f"ID: {student_id}, Name: {student_name}")

if not results:
    print("All students are enrolled.")

connection.close()
