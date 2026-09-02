# Level 1: IS-A Relationship - Question 8
# Create a Person class and derive Student and Teacher classes

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Email: {self.email}")


class Student(Person):
    def __init__(self, name, age, email, student_id, course):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.course = course
    
    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}, Course: {self.course}")


class Teacher(Person):
    def __init__(self, name, age, email, teacher_id, subject):
        super().__init__(name, age, email)
        self.teacher_id = teacher_id
        self.subject = subject
    
    def display(self):
        super().display()
        print(f"Teacher ID: {self.teacher_id}, Subject: {self.subject}")


# Example usage
student = Student("Alice", 20, "alice@example.com", "S001", "Python")
teacher = Teacher("Mr. Smith", 45, "smith@example.com", "T001", "Mathematics")

student.display()
print()
teacher.display()
