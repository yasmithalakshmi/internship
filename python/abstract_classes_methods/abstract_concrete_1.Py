#abstract Employee class with one abstract method calculate_salary() and one normal method display_company().
from abc import ABC, abstractmethod
class Employee:
    def display_company(self):
        print("abc company")

    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(Employee):
    def calculate_salary(self,salary):
        print("manager salary is:",salary)
class Developer(Employee):
    def calculate_salary(self,salary):
        print("developer salary is:",salary)
manager = Manager()
manager.display_company()
manager.calculate_salary(50000)

developer = Developer()
developer.display_company()
developer.calculate_salary(40000)
