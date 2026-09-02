# 1. Create a Student class with instance variables name, age, and course. Create three student objects.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Alice", 18, "BCA")
s2 = Student("Bob", 20, "BSc")
s3 = Student("Charlie", 19, "MBA")

print("Student 1:", s1.name, s1.age, s1.course)
print("Student 2:", s2.name, s2.age, s2.course)
print("Student 3:", s3.name, s3.age, s3.course)
