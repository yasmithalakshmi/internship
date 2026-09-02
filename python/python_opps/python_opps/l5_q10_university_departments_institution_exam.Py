# Level 5: Combined Relationships - Question 10
# University HAS-A Departments, IS-A EducationalInstitution, USES-A ExaminationService

class Department:
    def __init__(self, name):
        self.name = name


class ExaminationService:
    def conduct_exam(self):
        print("Exam conducted!")


class EducationalInstitution:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"Institution: {self.name}")


class University(EducationalInstitution):
    def __init__(self, name):
        super().__init__(name)
        self.departments = []
        self.examination_service = ExaminationService()
    
    def add_department(self, dept):
        self.departments.append(dept)
    
    def hold_exam(self):
        self.examination_service.conduct_exam()


# Example usage
university = University("MIT")
university.add_department(Department("Engineering"))
university.info()
university.hold_exam()
