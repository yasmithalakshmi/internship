import sqlite3

# Question 16: Find the highest and lowest marks

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

cursor.execute("SELECT MAX(marks), MIN(marks) FROM students")
result = cursor.fetchone()

highest = result[0]
lowest = result[1]

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")

connection.close()
