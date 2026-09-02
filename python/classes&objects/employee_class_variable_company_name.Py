# 2. Create an Employee class with a class variable company_name. Display the company name for multiple employees.

class Employee:
    company_name = "TechWorld"

    def __init__(self, name):
        self.name = name

emp1 = Employee("Amit")
emp2 = Employee("Neha")

print(emp1.name, Employee.company_name)
print(emp2.name, Employee.company_name)
