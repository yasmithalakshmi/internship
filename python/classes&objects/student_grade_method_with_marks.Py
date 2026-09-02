# 2. Create a Student class with a method that accepts marks and returns the grade.

class Student:
    def grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "D"

s = Student()
print(s.grade(80))
