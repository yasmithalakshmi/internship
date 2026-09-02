# 4. Create a Student class that automatically counts how many student objects have been created.

class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")
print("Total students created:", Student.count)
