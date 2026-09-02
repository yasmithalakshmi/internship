import sqlite3

# Question 5: Display only student names

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM students")
names = cursor.fetchall()

print("Student Names:")
for name in names:
    print(name[0])

connection.close()
