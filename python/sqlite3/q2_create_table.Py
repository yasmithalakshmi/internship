import sqlite3

# Question 2: Create a students table with: id, name, age, course, marks

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        marks REAL
    )
""")

connection.commit()
print("Table 'students' created successfully!")
connection.close()
