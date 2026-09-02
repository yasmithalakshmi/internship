# 2. Create a class with multiple instance methods where one method calls another method.

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

    def show(self):
        self.greet()

s = Student("Asha")
s.show()
