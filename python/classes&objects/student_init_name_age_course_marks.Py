# 1. Create a Student class using __init__() to initialize name, age, course, and marks.

class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

s = Student("Riya", 19, "BCA", 88)
print("Name:", s.name)
print("Age:", s.age)
print("Course:", s.course)
print("Marks:", s.marks)
