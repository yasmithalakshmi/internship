# Level 3: USES-A Relationship - Question 1
# Create a Student class and a Printer class

class Printer:
    def print_document(self, content):
        print(f"Printing: {content}")


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.printer = Printer()
    
    def print_details(self):
        details = f"Student Name: {self.name}, ID: {self.student_id}"
        self.printer.print_document(details)


# Example usage
student = Student("Alice", "S001")
student.print_details()
