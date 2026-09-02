# 2. Create an Employee class with instance variables name, department, and salary. Create five employee objects.

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

employees = [
    Employee("Naveen", "HR", 30000),
    Employee("Priya", "IT", 45000),
    Employee("Suresh", "Sales", 35000),
    Employee("Anu", "Finance", 50000),
    Employee("Raju", "Support", 28000)
]

for emp in employees:
    print(emp.name, emp.department, emp.salary)
