import sqlite3

# FINAL CHALLENGE: Build a Student Management System using Python + SQLite3
# Requirements: Functions, SQLite3, parameterized queries, exception handling, 
# commit(), rollback(), and a menu-driven interface

connection = sqlite3.connect("college.db")
cursor = connection.cursor()


def display_menu():
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Top Students")
    print("7. Course-wise Statistics")
    print("8. Average Marks")
    print("9. Student Count")
    print("10. Exit")
    choice = input("Enter your choice: ")
    return choice


def add_student():
    """Add a new student to the database"""
    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))
        
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
            (student_id, name, age, course, marks)
        )
        connection.commit()
        print("✓ Student added successfully!")
        
    except ValueError:
        print("✗ Invalid input! Please enter correct data types.")
        connection.rollback()
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")
        connection.rollback()


def view_all_students():
    """Display all students"""
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        
        if students:
            print("\n--- All Students ---")
            print("ID | Name | Age | Course | Marks")
            print("-" * 50)
            for student in students:
                print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]} | {student[4]}")
        else:
            print("No students found!")
            
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")


def search_student():
    """Search for a student"""
    try:
        print("\nSearch Options:")
        print("1. By ID")
        print("2. By Name")
        print("3. By Course")
        print("4. By Marks Range")
        
        search_choice = input("Select search option: ")
        
        if search_choice == "1":
            student_id = int(input("Enter Student ID: "))
            cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
            
        elif search_choice == "2":
            name = input("Enter Student Name (or part of it): ")
            cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("%" + name + "%",))
            
        elif search_choice == "3":
            course = input("Enter Course: ")
            cursor.execute("SELECT * FROM students WHERE course = ?", (course,))
            
        elif search_choice == "4":
            min_marks = float(input("Enter minimum marks: "))
            max_marks = float(input("Enter maximum marks: "))
            cursor.execute(
                "SELECT * FROM students WHERE marks BETWEEN ? AND ?",
                (min_marks, max_marks)
            )
        else:
            print("Invalid option!")
            return
        
        results = cursor.fetchall()
        
        if results:
            print("\n--- Search Results ---")
            for student in results:
                print(student)
        else:
            print("No students found!")
            
    except ValueError:
        print("✗ Invalid input!")
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")


def update_student():
    """Update student information"""
    try:
        student_id = int(input("Enter Student ID to update: "))
        
        print("What to update?")
        print("1. Marks")
        print("2. Course")
        print("3. Age")
        
        update_choice = input("Select option: ")
        
        if update_choice == "1":
            new_marks = float(input("Enter new marks: "))
            cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, student_id))
            
        elif update_choice == "2":
            new_course = input("Enter new course: ")
            cursor.execute("UPDATE students SET course = ? WHERE id = ?", (new_course, student_id))
            
        elif update_choice == "3":
            new_age = int(input("Enter new age: "))
            cursor.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))
        else:
            print("Invalid option!")
            return
        
        connection.commit()
        
        if cursor.rowcount > 0:
            print("✓ Student updated successfully!")
        else:
            print("✗ Student not found!")
            
    except ValueError:
        print("✗ Invalid input!")
        connection.rollback()
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")
        connection.rollback()


def delete_student():
    """Delete a student"""
    try:
        student_id = int(input("Enter Student ID to delete: "))
        confirm = input("Are you sure? (yes/no): ")
        
        if confirm.lower() == "yes":
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            connection.commit()
            
            if cursor.rowcount > 0:
                print("✓ Student deleted successfully!")
            else:
                print("✗ Student not found!")
        else:
            print("Deletion cancelled.")
            
    except ValueError:
        print("✗ Invalid input!")
        connection.rollback()
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")
        connection.rollback()


def show_top_students():
    """Display top students by marks"""
    try:
        num = int(input("How many top students to display? "))
        cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT ?", (num,))
        
        students = cursor.fetchall()
        
        if students:
            print(f"\n--- Top {num} Students ---")
            for student in students:
                print(student)
        else:
            print("No students found!")
            
    except ValueError:
        print("✗ Invalid input!")
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")


def course_statistics():
    """Display course-wise statistics"""
    try:
        cursor.execute("""
            SELECT course, COUNT(*), AVG(marks), MAX(marks), MIN(marks)
            FROM students
            GROUP BY course
        """)
        
        results = cursor.fetchall()
        
        if results:
            print("\n--- Course Statistics ---")
            print("Course | Count | Avg Marks | Highest | Lowest")
            print("-" * 55)
            for row in results:
                print(f"{row[0]} | {row[1]} | {row[2]:.2f} | {row[3]} | {row[4]}")
        else:
            print("No data available!")
            
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")


def average_marks():
    """Display average marks"""
    try:
        cursor.execute("SELECT AVG(marks) FROM students")
        avg = cursor.fetchone()[0]
        
        if avg:
            print(f"\n--- Average Marks ---")
            print(f"Average: {avg:.2f}")
        else:
            print("No students found!")
            
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")


def student_count():
    """Display total student count"""
    try:
        cursor.execute("SELECT COUNT(*) FROM students")
        count = cursor.fetchone()[0]
        
        print(f"\n--- Student Count ---")
        print(f"Total Students: {count}")
        
    except sqlite3.Error as error:
        print(f"✗ Database error: {error}")


# Main program loop
print("Welcome to Student Management System!")

while True:
    choice = display_menu()
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_top_students()
    elif choice == "7":
        course_statistics()
    elif choice == "8":
        average_marks()
    elif choice == "9":
        student_count()
    elif choice == "10":
        print("\nThank you for using Student Management System!")
        break
    else:
        print("✗ Invalid choice! Please try again.")

connection.close()
