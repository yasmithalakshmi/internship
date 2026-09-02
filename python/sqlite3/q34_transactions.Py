import sqlite3

# Question 34: Use SQLite transactions to insert/update multiple records safely

connection = sqlite3.connect("college.db")
cursor = connection.cursor()

print("Transaction Example: Safe insert/update of multiple records\n")

try:
    print("Starting transaction...")
    
    # Insert multiple records in one transaction
    students_to_insert = [
        (50, "TransStudent1", 20, "Python", 88),
        (51, "TransStudent2", 21, "Java", 85),
        (52, "TransStudent3", 19, "SQL", 92),
        (53, "TransStudent4", 22, "Web Development", 78),
    ]
    
    cursor.executemany(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
        students_to_insert
    )
    
    print(f"Inserted {len(students_to_insert)} students")
    
    # Update multiple records
    cursor.execute("UPDATE students SET marks = marks + 5 WHERE course = ?", ("Python",))
    
    print(f"Updated {cursor.rowcount} Python students")
    
    # Commit the transaction
    connection.commit()
    print("\nTransaction committed successfully!")
    
except sqlite3.Error as error:
    print(f"Error occurred: {error}")
    connection.rollback()
    print("Transaction rolled back!")

finally:
    print("\nFinal student count:")
    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]
    print(f"Total students: {total}")
    
    connection.close()
