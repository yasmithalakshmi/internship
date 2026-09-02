# Level 4: Identify the Relationship - Question 8
# A Teacher is a Person - IS-A Relationship (Inheritance)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} teaches {self.subject}")


# Example usage
teacher = Teacher("Mr. Smith", 45, "Mathematics")
teacher.teach()
