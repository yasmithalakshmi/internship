# Level 1: IS-A Relationship - Question 4
# Create an Employee class and a Manager class

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department
    
    def display(self):
        super().display()
        print(f"Department: {self.department}")


# Example usage
manager = Manager("John", "M001", 50000, "HR")
manager.display()
