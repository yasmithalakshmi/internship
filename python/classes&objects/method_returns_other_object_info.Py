# 3. Create a class with a method that returns another object's information.

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def info(self):
        return self.name + " studies " + self.course

class School:
    def __init__(self, student):
        self.student = student

    def display_student(self):
        print(self.student.info())

s = Student("Divya", "BCA")
school = School(s)
school.display_student()
