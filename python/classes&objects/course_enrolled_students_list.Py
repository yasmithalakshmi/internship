# 9. Create a Course class that stores enrolled students and provides a method to display them.

class Course:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)

    def display_students(self):
        for name in self.students:
            print(name)

course = Course()
course.add_student("Asha")
course.add_student("Ravi")
course.add_student("Neha")
course.display_students()
