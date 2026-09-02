import sqlite3

# Question 13: Display the top 3 students

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
students = cursor.fetchall()

print("Top 3 students:")
for student in students:
    print(student)

connection.close()
