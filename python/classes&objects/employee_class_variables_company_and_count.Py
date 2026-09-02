# 8. Create an Employee class with class variables company_name and employee_count.

class Employee:
    company_name = "Infosys"
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

emp1 = Employee("Sunita")
emp2 = Employee("Ramesh")

print(Employee.company_name)
print(Employee.employee_count)
