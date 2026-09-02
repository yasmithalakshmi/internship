# 8. Create a Student class with methods to calculate total marks and average marks.

class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def total_marks(self):
        return self.marks1 + self.marks2 + self.marks3

    def average_marks(self):
        return self.total_marks() / 3

s = Student(80, 90, 85)
print("Total marks:", s.total_marks())
print("Average marks:", s.average_marks())
