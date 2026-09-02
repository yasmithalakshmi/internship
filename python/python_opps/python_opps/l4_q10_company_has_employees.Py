# Level 4: Identify the Relationship - Question 10
# A Company has Employees - HAS-A Relationship (Aggregation)

class Employee:
    def __init__(self, name):
        self.name = name


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []
    
    def hire_employee(self, employee):
        self.employees.append(employee)
    
    def show_employees(self):
        print(f"Company: {self.company_name}")
        for emp in self.employees:
            print(f"  - {emp.name}")


# Example usage
company = Company("Tech Corp")
company.hire_employee(Employee("John"))
company.hire_employee(Employee("Jane"))
company.show_employees()
