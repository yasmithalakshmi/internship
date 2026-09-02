# 1. Create a Student class with a class variable college_name. Create three student objects and display the college name.

class Student:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Sneha")
s3 = Student("Deepak")

print(s1.name, Student.college_name)
print(s2.name, Student.college_name)
print(s3.name, Student.college_name)
