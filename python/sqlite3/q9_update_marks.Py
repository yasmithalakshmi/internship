import sqlite3

# Question 9: Update the marks of one student

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

student_id = int(input("Enter student ID to update: "))
new_marks = float(input("Enter new marks: "))

cursor.execute("UPDATE students SET marks = ? WHERE id = ?", (new_marks, student_id))

connection.commit()

if cursor.rowcount > 0:
    print("Marks updated successfully!")
else:
    print("Student not found!")

connection.close()
