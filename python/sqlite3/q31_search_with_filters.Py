import sqlite3

# Question 31: Create a student search feature with multiple filters

def search_students(db_name="college.db", name=None, course=None, min_marks=None, max_marks=None):
    """Search students with multiple filter options"""
    
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    query = "SELECT * FROM students WHERE 1 = 1"
    parameters = []
    
    if name:
        query += " AND name LIKE ?"
        parameters.append("%" + name + "%")
    
    if course:
        query += " AND course = ?"
        parameters.append(course)
    
    if min_marks:
        query += " AND marks >= ?"
        parameters.append(min_marks)
    
    if max_marks:
        query += " AND marks <= ?"
        parameters.append(max_marks)
    
    try:
        cursor.execute(query, parameters)
        results = cursor.fetchall()
        
        print("Search Results:")
        for student in results:
            print(student)
        
        if not results:
            print("No students found matching the criteria.")
    
    except sqlite3.Error as error:
        print("Search error:", error)
    
    finally:
        connection.close()


# Example usage
if __name__ == "__main__":
    print("Search by name 'A':")
    search_students(name="A")
    
    print("\nSearch by course 'Python':")
    search_students(course="Python")
    
    print("\nSearch by marks between 75 and 95:")
    search_students(min_marks=75, max_marks=95)
    
    print("\nSearch by name 'Student' and marks >= 80:")
    search_students(name="Student", min_marks=80)
