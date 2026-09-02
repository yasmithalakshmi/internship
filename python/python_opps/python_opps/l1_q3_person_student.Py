# Level 1: IS-A Relationship - Question 3
# Create a Person class and a Student class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    
    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}, Course: {self.course}")


# Example usage
student = Student("Alice", 20, "S001", "Python")
student.display()
