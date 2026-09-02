# 3. Create a class called Employee and create an object to represent an employee.

class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

emp = Employee("Rahul", "IT", 45000)
print("Employee Name:", emp.name)
print("Department:", emp.department)
print("Salary:", emp.salary)
