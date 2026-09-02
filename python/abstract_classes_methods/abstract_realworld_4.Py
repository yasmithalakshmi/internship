# abstract UniversityCourse class and implement Engineering, Medical, and Management courses.
from abc import ABC, abstractmethod
class UniversityCourse(ABC):
    @abstractmethod
    def course_details(self):
        pass
class Engineering(UniversityCourse):
    def course_details(self):
        print("Engineering course includes subjects like Mathematics, Physics, and Computer Science.")
class BBA(UniversityCourse):
    def course_details(self):
        print("BBA course includes subjects like Business Management, Marketing, and Finance.")
class pharmacy(UniversityCourse):
    def course_details(self):
        print("Pharmacy course includes subjects like Pharmacology, Medicinal Chemistry, and Pharmaceutics.")
Engineering().course_details()
BBA().course_details()
pharmacy().course_details()