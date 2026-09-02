import sqlite3

# Question 3: Insert 5 student records

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

students = [
    (1, "Anu", 20, "Python", 88),
    (2, "Bharath", 21, "Java", 74),
    (3, "Arun", 19, "Python", 93),
    (4, "Diya", 22, "SQL", 67),
    (5, "Farhan", 20, "Web Development", 81)
]

for student in students:
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", student)

connection.commit()
print("5 student records inserted successfully!")
connection.close()
