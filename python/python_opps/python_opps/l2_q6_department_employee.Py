# Level 2: HAS-A Relationship - Question 6
# Create a Department class that HAS-A multiple Employee objects

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def info(self):
        print(f"  Employee: {self.name} (ID: {self.emp_id}, Salary: {self.salary})")


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []
    
    def hire_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        print(f"Department: {self.dept_name}")
        print("Employees:")
        for emp in self.employees:
            emp.info()


# Example usage
dept = Department("Engineering")
dept.hire_employee(Employee("John", "E001", 60000))
dept.hire_employee(Employee("Jane", "E002", 65000))
dept.hire_employee(Employee("Bob", "E003", 70000))
dept.display_employees()
