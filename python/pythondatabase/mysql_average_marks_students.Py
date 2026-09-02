# Beginner-level: Find the average marks of students

import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="college_db"
)

# Create a cursor to run SQL commands
cursor = connection.cursor()

# SQL query to calculate average marks
query = "SELECT AVG(marks) FROM students"

# Run the query
cursor.execute(query)

# Get the result
result = cursor.fetchone()

# Print the answer
print("Average marks:", result[0])

# Close the connection
connection.close()

