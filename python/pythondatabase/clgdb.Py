import sqlite3
# Question 1: Create a SQLite database named college.db.
connection = sqlite3.connect("college.db")
cursor = connection.cursor()

# Question 2: Create a students table.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        course TEXT,
        marks REAL
    )
""")
connection.commit()

# Question 3: Insert five student records.
students = [
    (1, "Anu", 20, "Python", 88),
    (2, "yashu", 21, "Java", 74),
    (3, "manu", 19, "Python", 93),
    (4, "teju", 22, "SQL", 67),
    (5, "rohanth", 20, "Web Development", 81)
]

for student in students:
    try:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
    except sqlite3.IntegrityError:
        pass
connection.commit()

# Question 4: Display all students.
print("\nQuestion 4: All students")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# Question 5: Display only student names.
print("\nQuestion 5: Student names")
cursor.execute("SELECT name FROM students")
print(cursor.fetchall())

# Question 6: Display students who scored more than 75.
print("\nQuestion 6: Students with marks above 75")
cursor.execute("SELECT * FROM students WHERE marks > ?", (75,))
print(cursor.fetchall())

# Question 7: Find students in the Python course.
print("\nQuestion 7: Python students")
cursor.execute("SELECT * FROM students WHERE course = ?", ("Python",))
print(cursor.fetchall())

# Question 8: Find a student using an ID.
print("\nQuestion 8: Student with ID 1")
cursor.execute("SELECT * FROM students WHERE id = ?", (1,))
print(cursor.fetchone())


# Question 9: Update one student's marks.
try:
    cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (90, 1))
    connection.commit()
    print("\nQuestion 9: Marks updated")
except sqlite3.Error as error:
    connection.rollback()
    print(error)
    
# Question 10: Delete one student.
try:
    student_id = int(input("\nQuestion 10 - Enter the student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    
# Question 11: Insert 10 students using executemany().
ten_students = [
    (10, "abhi", 18, "Python", 70),
    (11, "rupa", 19, "Python", 71),
    (12, "harsha", 20, "Java", 72),
    (13, "varshi", 18, "SQL", 73),
    (14, "hepzii", 19, "Python", 74),
    (15, "prasanna", 20, "Java", 75),
    (16, "kumari", 18, "SQL", 76),
    (17, "ammu", 19, "Python", 77),
    (18, "pooja", 20, "Java", 78),
    (19, "anurag", 18, "SQL", 79)
]

# This function can be called from the menu at the bottom.
def insert_ten_students():
    try:
        cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", ten_students)
        connection.commit()
        print("10 students inserted.")
    except sqlite3.Error as error:
        connection.rollback()
        print("Insert failed. Rollback completed:", error)


# Question 12: Display students in descending order of marks.
def marks_descending():
    cursor.execute("SELECT * FROM students ORDER BY marks DESC")
    print(cursor.fetchall())


# Question 13: Display the top 3 students.
def top_three_students():
    cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
    print(cursor.fetchall())


# Question 14: Count the students.
def student_count():
    cursor.execute("SELECT COUNT(*) FROM students")
    print("Total students:", cursor.fetchone()[0])


# Questions 15 and 16: Find average, highest, and lowest marks.
def marks_statistics():
    cursor.execute("SELECT AVG(marks), MAX(marks), MIN(marks) FROM students")
    print("Average, highest, lowest:", cursor.fetchone())


# Question 17: Count students course-wise.
def count_by_course():
    cursor.execute("SELECT course, COUNT(*) FROM students GROUP BY course")
    print(cursor.fetchall())


# Question 18: Find average marks for each course.
def average_by_course():
    cursor.execute("SELECT course, AVG(marks) FROM students GROUP BY course")
    print(cursor.fetchall())


# Question 19: Find names starting with A.
def names_starting_with_a():
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("A%",))
    print(cursor.fetchall())


# Question 20: Find marks between 60 and 90.
def marks_between_60_and_90():
    cursor.execute("SELECT * FROM students WHERE marks BETWEEN ? AND ?", (60, 90))
    print(cursor.fetchall())

# Questions 25 and 26: Create courses and enrollments tables.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT UNIQUE
    )
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")
connection.commit()

# Add courses and enrollment records for the JOIN examples.
cursor.execute("INSERT OR IGNORE INTO courses (course_name) SELECT DISTINCT course FROM students")
cursor.execute("""
    INSERT INTO enrollments (student_id, course_id)
    SELECT students.id, courses.course_id
    FROM students JOIN courses ON students.course = courses.course_name
    WHERE NOT EXISTS (
        SELECT * FROM enrollments WHERE enrollments.student_id = students.id
    )
""")
connection.commit()

# Question 27: Display student names with course names using JOIN.
def student_course_join():
    cursor.execute("""
        SELECT students.name, courses.course_name
        FROM students
        JOIN enrollments ON students.id = enrollments.student_id
        JOIN courses ON enrollments.course_id = courses.course_id
    """)
    print(cursor.fetchall())


# Question 28: Find students who are not enrolled in a course.
def students_without_course():
    cursor.execute("""
        SELECT students.name
        FROM students
        LEFT JOIN enrollments ON students.id = enrollments.student_id
        WHERE enrollments.student_id IS NULL
    """)
    print(cursor.fetchall())


# Question 29: Find the number of students in each course.
def enrolled_count_by_course():
    cursor.execute("""
        SELECT courses.course_name, COUNT(enrollments.student_id)
        FROM courses
        LEFT JOIN enrollments ON courses.course_id = enrollments.course_id
        GROUP BY courses.course_id
    """)
    print(cursor.fetchall())


# Question 30: A small Database class containing CRUD methods.
class Database:
    def add_student(self, student):
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
        connection.commit()

    def view_students(self):
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

    def update_marks(self, student_id, marks):
        cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
        connection.commit()

    def delete_student(self, student_id):
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()


# Question 31: Search using more than one filter.
def search_students():
    name = input("Enter name (blank for any): ")
    course = input("Enter course (blank for any): ")
    cursor.execute("""
        SELECT * FROM students
        WHERE name LIKE ? AND course LIKE ?
    """, ("%" + name + "%", "%" + course + "%"))
    print(cursor.fetchall())


# Question 32: Pagination using LIMIT and OFFSET.
def show_page():
    limit = int(input("How many records: "))
    offset = int(input("Starting position: "))
    cursor.execute("SELECT * FROM students LIMIT ? OFFSET ?", (limit, offset))
    print(cursor.fetchall())


# Question 33: Create an index and view its query plan.
cursor.execute("CREATE INDEX IF NOT EXISTS student_name_index ON students(name)")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM students WHERE name = ?", ("Anu",))
print("\nQuestion 33: Query plan")
print(cursor.fetchall())


# Question 34: Insert or update multiple records in one transaction.
def safe_transaction():
    try:
        cursor.execute("UPDATE students SET marks = marks + ? WHERE course = ?", (1, "Python"))
        cursor.execute("UPDATE students SET marks = marks + ? WHERE course = ?", (1, "Java"))
        connection.commit()
        print("Both updates were saved.")
    except sqlite3.Error as error:
        connection.rollback()
        print("Transaction failed. All changes were cancelled:", error)

# Final challenge: Student Management System menu.
def menu():
    while True:
        print("""
1. Add student
2. View all students
3. Search student
4. Update marks
5. Delete student
6. Show top students
7. Course-wise statistics
8. Average marks
9. Student count
10. Insert 10 students
11. Show advanced JOIN reports
12. Show one page of students
0. Exit
""")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                student = (
                    int(input("ID: ")), input("Name: "), int(input("Age: ")),
                    input("Course: "), float(input("Marks: "))
                )
                cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)
                connection.commit()
                print("Student added.")
            elif choice == "2":
                cursor.execute("SELECT * FROM students")
                print(cursor.fetchall())
            elif choice == "3":
                search_students()
            elif choice == "4":
                student_id = int(input("Student ID: "))
                marks = float(input("New marks: "))
                cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (marks, student_id))
                connection.commit()
                print("Student updated.")
            elif choice == "5":
                student_id = int(input("Student ID: "))
                cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
                connection.commit()
                print("Student deleted.")
            elif choice == "6":
                top_three_students()
            elif choice == "7":
                count_by_course()
                average_by_course()
            elif choice == "8":
                marks_statistics()
            elif choice == "9":
                student_count()
            elif choice == "10":
                insert_ten_students()
            elif choice == "11":
                student_course_join()
                students_without_course()
                enrolled_count_by_course()
            elif choice == "12":
                show_page()
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (ValueError, sqlite3.Error) as error:
            connection.rollback()
            print("Error:", error)


# Run the menu.
menu()
connection.close()

