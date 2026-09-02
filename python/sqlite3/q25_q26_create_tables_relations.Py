import sqlite3

# Question 25: Create three tables: students, courses, and enrollments
# Question 26: Establish relationships using primary and foreign keys

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

# Students table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        marks REAL
    )
""")

# Courses table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT UNIQUE NOT NULL
    )
""")

# Enrollments table with foreign keys
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")

connection.commit()
print("Three tables created with relationships!")
connection.close()
