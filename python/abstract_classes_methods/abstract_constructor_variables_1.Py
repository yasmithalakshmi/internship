#abstract class Employee with a constructor that accepts name and employee ID. Add an abstract method calculate_salary().
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self,salary):
        pass
class Manager(Employee):
    def calculate_salary(self, salary):
        print(f"salary of Manager {self.name} with ID {self.employee_id} is: {salary}")
class Developer(Employee):
    def calculate_salary(self, salary):
        print(f"salary of Developer {self.name} with ID {self.employee_id} is: {salary}")
manager = Manager("manu", 101)
developer = Developer("yashu", 102)
manager.calculate_salary(50000)
developer.calculate_salary(40000)