import sqlite3

# Question 18: Find the average marks for each course

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT course, AVG(marks) FROM students GROUP BY course")
results = cursor.fetchall()

print("Average marks by course:")
for course, average in results:
    print(f"{course}: {average}")

connection.close()
