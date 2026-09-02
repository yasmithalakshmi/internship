# 2. Create an Employee class using __init__() to initialize employee ID, name, department, and salary.

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

emp = Employee(101, "Nisha", "HR", 42000)
print("Employee ID:", emp.emp_id)
print("Name:", emp.name)
print("Department:", emp.department)
print("Salary:", emp.salary)
