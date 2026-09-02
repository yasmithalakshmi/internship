# 1. Create a Student class with a method display() to display student details.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

s = Student("Amit", 20, "BCA")
s.display()
