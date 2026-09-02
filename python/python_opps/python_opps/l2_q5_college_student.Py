# Level 2: HAS-A Relationship - Question 5
# Create a College class that HAS-A multiple Student objects

class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
    
    def info(self):
        print(f"  Student: {self.name} (ID: {self.student_id}, Course: {self.course})")


class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []
    
    def enroll_student(self, student):
        self.students.append(student)
    
    def display_students(self):
        print(f"College: {self.college_name}")
        print("Enrolled Students:")
        for student in self.students:
            student.info()


# Example usage
college = College("MIT")
college.enroll_student(Student("Alice", "S001", "Python"))
college.enroll_student(Student("Bob", "S002", "Java"))
college.enroll_student(Student("Charlie", "S003", "Data Science"))
college.display_students()
