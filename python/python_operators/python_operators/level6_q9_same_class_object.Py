# Level 6 - Question 9
# Create two objects of the same class and check whether they refer to the same object.

class Student:
    pass

s1 = Student()
s2 = Student()
print(s1 is s2)
