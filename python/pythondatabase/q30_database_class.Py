import sqlite3

# Question 30: Create a Python Database class containing CRUD methods

class Database:
    def __init__(self, db_name="college.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
    
    def create(self, student_id, name, age, course, marks):
        """Create a new student record"""
        try:
            self.cursor.execute(
                "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
                (student_id, name, age, course, marks)
            )
            self.connection.commit()
            print("Student added successfully!")
        except sqlite3.Error as error:
            print("Error adding student:", error)
            self.connection.rollback()
    
    def read(self, student_id=None):
        """Read student records"""
        try:
            if student_id:
                self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
                return self.cursor.fetchone()
            else:
                self.cursor.execute("SELECT * FROM students")
                return self.cursor.fetchall()
        except sqlite3.Error as error:
            print("Error reading students:", error)
            return None
    
    def update(self, student_id, marks):
        """Update student marks"""
        try:
            self.cursor.execute(
                "UPDATE students SET marks = ? WHERE id = ?",
                (marks, student_id)
            )
            self.connection.commit()
            if self.cursor.rowcount > 0:
                print("Student updated successfully!")
            else:
                print("Student not found!")
        except sqlite3.Error as error:
            print("Error updating student:", error)
            self.connection.rollback()
    
    def delete(self, student_id):
        """Delete a student record"""
        try:
            self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            self.connection.commit()
            if self.cursor.rowcount > 0:
                print("Student deleted successfully!")
            else:
                print("Student not found!")
        except sqlite3.Error as error:
            print("Error deleting student:", error)
            self.connection.rollback()
    
    def close(self):
        """Close the database connection"""
        self.connection.close()


# Example usage
if __name__ == "__main__":
    db = Database()
    
    # Create
    db.create(100, "TestStudent", 20, "Python", 85)
    
    # Read
    print("\nAll students:")
    for student in db.read():
        print(student)
    
    # Update
    db.update(100, 90)
    
    # Read specific
    print("\nStudent with ID 100:")
    print(db.read(100))
    
    # Delete
    db.delete(100)
    
    db.close()
