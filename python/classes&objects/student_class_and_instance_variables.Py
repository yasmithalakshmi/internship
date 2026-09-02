# 7. Create a Student class with a class variable representing the school/college name and an instance variable representing the student's name.

class Student:
    college_name = "Global College"

    def __init__(self, name):
        self.name = name

s1 = Student("Riya")
s2 = Student("Rohit")

print(s1.name, Student.college_name)
print(s2.name, Student.college_name)
