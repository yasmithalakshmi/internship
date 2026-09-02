import sqlite3

# Question 21: Create a menu-driven CRUD application
# Question 22: Add exception handling using try-except
# Question 23: Use parameterized queries for all user inputs
# Question 24: Implement commit() and rollback()

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

def display_menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Marks")
    print("5. Delete Student")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_student():
    try:
        student_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))
        
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", 
                      (student_id, name, age, course, marks))
        connection.commit()
        print("Student added successfully!")
    except ValueError:
        print("Invalid input! Please enter correct data type.")
        connection.rollback()
    except sqlite3.Error as error:
        print("Database error:", error)
        connection.rollback()

def view_students():
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print("\nAll Students:")
        for student in students:
            print(student)
    except sqlite3.Error as error:
        print("Database error:", error)

def search_student():
    try:
        student_id = int(input("Enter student ID: "))
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        
        if student:
            print("Student found:", student)
        else:
            print("Student not found!")
    except ValueError:
        print("Invalid ID! Please enter a number.")
    except sqlite3.Error as error:
        print("Database error:", error)

def update_marks():
    try:
        student_id = int(input("Enter student ID: "))
        new_marks = float(input("Enter new marks: "))
        
        cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, student_id))
        connection.commit()
        
        if cursor.rowcount > 0:
            print("Marks updated successfully!")
        else:
            print("Student not found!")
    except ValueError:
        print("Invalid input! Please enter correct data type.")
        connection.rollback()
    except sqlite3.Error as error:
        print("Database error:", error)
        connection.rollback()

def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()
        
        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    except ValueError:
        print("Invalid ID! Please enter a number.")
        connection.rollback()
    except sqlite3.Error as error:
        print("Database error:", error)
        connection.rollback()

# Main loop
while True:
    choice = display_menu()
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")

connection.close()
