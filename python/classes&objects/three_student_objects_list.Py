# 1. Create a Student class with instance variables name, age, and course. Create three student objects.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

students = [
    Student("Asha", 18, "BCA"),
    Student("Kiran", 20, "BSc"),
    Student("Meena", 19, "MBA")
]

for student in students:
    print(student.name, student.age, student.course)
