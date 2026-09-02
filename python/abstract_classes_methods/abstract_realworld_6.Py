#abstract EmployeePayroll class and implement FullTimeEmployee, PartTimeEmployee, and ContractEmployee.
from abc import ABC, abstractmethod
class EmployeePayroll(ABC):
    @abstractmethod
    def calculate_salary(self, hours_worked):
        pass
class FullTimeEmployee(EmployeePayroll):
    def calculate_salary(self, hours_worked):
        salary = hours_worked * 2000
        print(f"Full-time employee salary: {salary}/-")

class PartTimeEmployee(EmployeePayroll):
    def calculate_salary(self, hours_worked):
        salary = hours_worked * 1500
        print(f"Part-time employee salary: {salary}/-")

class ContractEmployee(EmployeePayroll):
    def calculate_salary(self, hours_worked):
        salary = hours_worked * 2500
        print(f"Contract employee salary:{salary}/-")

FullTimeEmployee().calculate_salary(40)
PartTimeEmployee().calculate_salary(20)
ContractEmployee().calculate_salary(30)