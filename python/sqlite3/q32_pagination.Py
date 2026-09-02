import sqlite3

# Question 32: Add pagination using LIMIT and OFFSET

def paginate_students(db_name="college.db", page=1, page_size=5):
    """Display students with pagination"""
    
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    
    offset = (page - 1) * page_size
    
    try:
        # Get total count
        cursor.execute("SELECT COUNT(*) FROM students")
        total_count = cursor.fetchone()[0]
        
        # Get paginated results
        cursor.execute(
            "SELECT * FROM students ORDER BY id LIMIT ? OFFSET ?",
            (page_size, offset)
        )
        
        results = cursor.fetchall()
        
        print(f"Page {page} (Showing {len(results)} of {total_count} students):")
        for student in results:
            print(student)
        
        total_pages = (total_count + page_size - 1) // page_size
        print(f"Total pages: {total_pages}")
    
    except sqlite3.Error as error:
        print("Pagination error:", error)
    
    finally:
        connection.close()


# Example usage
if __name__ == "__main__":
    print("Page 1:")
    paginate_students(page=1, page_size=3)
    
    print("\nPage 2:")
    paginate_students(page=2, page_size=3)
    
    print("\nPage 3:")
    paginate_students(page=3, page_size=3)
