import sqlite3

# Question 27: Display student names along with their course names using JOIN

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# First, insert courses
cursor.execute("INSERT OR IGNORE INTO courses (course_name) VALUES (?)", ("Python",))
cursor.execute("INSERT OR IGNORE INTO courses (course_name) VALUES (?)", ("Java",))
cursor.execute("INSERT OR IGNORE INTO courses (course_name) VALUES (?)", ("SQL",))
cursor.execute("INSERT OR IGNORE INTO courses (course_name) VALUES (?)", ("Web Development",))

connection.commit()

# Insert enrollments for students
cursor.execute("""
    INSERT OR IGNORE INTO enrollments (student_id, course_id)
    SELECT students.id, courses.course_id
    FROM students JOIN courses ON students.course = courses.course_name
""")

connection.commit()

# JOIN: Display student names with course names
cursor.execute("""
    SELECT students.name, courses.course_name
    FROM students
    JOIN enrollments ON students.id = enrollments.student_id
    JOIN courses ON enrollments.course_id = courses.course_id
""")

results = cursor.fetchall()

print("Student names with their course names:")
for student_name, course_name in results:
    print(f"{student_name} - {course_name}")

connection.close()
