import sqlite3

# Question 6: Display students who scored more than 75 marks

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students WHERE marks > ?", (75,))
students = cursor.fetchall()

print("Students with marks > 75:")
for student in students:
    print(student)

connection.close()
-