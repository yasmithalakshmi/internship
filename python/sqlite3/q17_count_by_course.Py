import sqlite3

# Question 17: Count students course-wise using GROUP BY

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT course, COUNT(*) FROM students GROUP BY course")
results = cursor.fetchall()

print("Students count by course:")
for course, count in results:
    print(f"{course}: {count}")

connection.close()
