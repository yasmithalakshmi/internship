# Level 4: Identify the Relationship - Question 3
# A Student uses a Printer - USES-A Relationship (Dependency)

class Printer:
    def print_text(self, text):
        print(f"Printing: {text}")


class Student:
    def __init__(self, name, printer):
        self.name = name
        self.printer = printer
    
    def print_assignment(self):
        self.printer.print_text(f"Assignment of {self.name}")


# Example usage
printer = Printer()
student = Student("Alice", printer)
student.print_assignment()
