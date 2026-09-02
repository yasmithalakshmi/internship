# 7. Create a Student class using __init__() and a method to calculate grade based on marks.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

s = Student("Anita", 82)
print(s.name, "got grade", s.calculate_grade())
