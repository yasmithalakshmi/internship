# Level 3: USES-A Relationship - Question 4
# Create an Employee and ReportGenerator class

class ReportGenerator:
    def generate_report(self, data):
        print(f"Generating report with data: {data}")
        print("Report generated successfully!")


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        self.report_generator = ReportGenerator()
    
    def create_report(self):
        data = f"Employee {self.name} ({self.emp_id})"
        self.report_generator.generate_report(data)


# Example usage
employee = Employee("John", "E001")
employee.create_report()
