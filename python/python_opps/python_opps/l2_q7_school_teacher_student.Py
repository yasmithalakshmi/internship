# Level 2: HAS-A Relationship - Question 7
# Create a School class that HAS-A Teacher and Student objects

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def info(self):
        print(f"  Teacher: {self.name} (Subject: {self.subject})")


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def info(self):
        print(f"  Student: {self.name} (Roll: {self.roll_no})")


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.teachers = []
        self.students = []
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_student(self, student):
        self.students.append(student)
    
    def display_info(self):
        print(f"School: {self.school_name}")
        print("Teachers:")
        for teacher in self.teachers:
            teacher.info()
        print("Students:")
        for student in self.students:
            student.info()


# Example usage
school = School("ABC School")
school.add_teacher(Teacher("Mr. Smith", "Math"))
school.add_teacher(Teacher("Ms. Johnson", "English"))
school.add_student(Student("Alice", 1))
school.add_student(Student("Bob", 2))
school.display_info()
