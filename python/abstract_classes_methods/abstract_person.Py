# abstract class Person with an abstract method role(). Implement it using Student and Teacher.
from abc import ABC, abstractmethod
class Person(ABC):
    @abstractmethod
    def role(self):
        pass
class Student(Person):
    def role(self):
        print("I am a student.")
class Teacher(Person):
    def role(self):
        print("I am a teacher.")
Student().role()
Teacher().role()
