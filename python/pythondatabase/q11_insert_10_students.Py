import sqlite3

# Question 11: Insert 10 students using executemany()

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

students = [
    (6, "Student6", 20, "Python", 85),
    (7, "Student7", 21, "Java", 78),
    (8, "Student8", 19, "Python", 92),
    (9, "Student9", 22, "SQL", 71),
    (10, "Student10", 20, "Web Development", 88),
    (11, "Student11", 21, "Python", 95),
    (12, "Student12", 20, "Java", 76),
    (13, "Student13", 19, "SQL", 82),
    (14, "Student14", 22, "Web Development", 79),
    (15, "Student15", 21, "Python", 90)
]

cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?, ?)", students)

connection.commit()
print("10 students inserted successfully using executemany()!")
connection.close()
