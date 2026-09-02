# 10. Create a menu-driven program that allows users to perform database CRUD operations.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

cursor = mydb.cursor()

while True:
    print("\n1. Insert Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))
        sql = "INSERT INTO students (name, age, course, marks) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, age, course, marks))
        mydb.commit()
        print("Student added.")
    elif choice == '2':
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)
    elif choice == '3':
        print("Update operation selected.")
    elif choice == '4':
        print("Delete operation selected.")
    elif choice == '5':
        break
    else:
        print("Invalid option")

