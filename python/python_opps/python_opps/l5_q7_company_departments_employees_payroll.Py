# Level 5: Combined Relationships - Question 7
# Company HAS-A Departments and Employees, USES-A PayrollService

class Department:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, name):
        self.name = name


class PayrollService:
    def process_payroll(self, amount):
        print(f"Processing payroll: ${amount}")


class Company:
    def __init__(self):
        self.departments = []
        self.employees = []
        self.payroll_service = PayrollService()
    
    def add_department(self, dept):
        self.departments.append(dept)
    
    def add_employee(self, emp):
        self.employees.append(emp)
    
    def pay_employees(self):
        amount = len(self.employees) * 5000
        self.payroll_service.process_payroll(amount)


# Example usage
company = Company()
company.add_department(Department("Engineering"))
company.add_employee(Employee("John"))
company.add_employee(Employee("Jane"))
company.pay_employees()
