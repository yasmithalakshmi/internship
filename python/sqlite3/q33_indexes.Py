import sqlite3

# Question 33: Create indexes and investigate their effect on queries

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

print("Creating indexes for better query performance...\n")

# Create indexes
cursor.execute("CREATE INDEX IF NOT EXISTS idx_name ON students(name)")
print("Index created on 'name' column")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_marks ON students(marks)")
print("Index created on 'marks' column")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_course ON students(course)")
print("Index created on 'course' column")

connection.commit()

print("\n--- Query Plans (Without and With Indexes) ---\n")

# Check query plan for search by name
print("Query Plan for searching by name:")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM students WHERE name LIKE ?", ("A%",))
for row in cursor.fetchall():
    print(row)

print("\nQuery Plan for searching by marks:")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM students WHERE marks > ?", (80,))
for row in cursor.fetchall():
    print(row)

print("\nQuery Plan for searching by course:")
cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM students WHERE course = ?", ("Python",))
for row in cursor.fetchall():
    print(row)

print("\nIndexes created! These speed up queries on frequently searched columns.")

connection.close()
