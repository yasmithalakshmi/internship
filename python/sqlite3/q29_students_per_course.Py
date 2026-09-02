import sqlite3

# Question 29: Find the number of students in each course

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    SELECT courses.course_name, COUNT(enrollments.student_id) AS student_count
    FROM courses
    LEFT JOIN enrollments ON courses.course_id = enrollments.course_id
    GROUP BY courses.course_id
""")

results = cursor.fetchall()

print("Number of students in each course:")
for course_name, student_count in results:
    print(f"{course_name}: {student_count} students")

connection.close()
