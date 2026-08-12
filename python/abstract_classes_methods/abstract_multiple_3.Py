#abstract class Employee with abstract methods calculate_salary() and display_details(). Implement them in Manager and Developer.
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass
class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for Manager.")

    def display_details(self):
        print("Displaying details of Manager.")
class Developer(Employee):
    def calculate_salary(self):
        print("Calculating salary for Developer.")

    def display_details(self):
        print("Displaying details of Developer.")
Manager().calculate_salary()
Manager().display_details()
Developer().calculate_salary()
Developer().display_details()