# 1. Create a class with both class variables and instance variables and demonstrate the difference between them.

class Example:
    college_name = "ABC College"

    def __init__(self, name):
        self.name = name

obj1 = Example("Sam")
obj2 = Example("John")

print(obj1.name)
print(obj1.college_name)
print(obj2.name)
print(Example.college_name)
