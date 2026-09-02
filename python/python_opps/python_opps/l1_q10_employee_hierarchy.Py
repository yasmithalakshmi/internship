# Level 1: IS-A Relationship - Question 10
# Create an Employee class and derive Developer, Tester, and Manager classes

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language
    
    def display(self):
        super().display()
        print(f"Language: {self.programming_language}")


class Tester(Employee):
    def __init__(self, name, emp_id, salary, testing_tool):
        super().__init__(name, emp_id, salary)
        self.testing_tool = testing_tool
    
    def display(self):
        super().display()
        print(f"Testing Tool: {self.testing_tool}")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Example usage
dev = Developer("John", "E001", 60000, "Python")
tester = Tester("Jane", "E002", 50000, "Selenium")
manager = Manager("Bob", "E003", 80000, "Engineering")

dev.display()
print()
tester.display()
print()
manager.display()
