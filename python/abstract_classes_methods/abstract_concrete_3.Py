#abstract Report class with an abstract method generate() and a normal method display_report_info().
from abc import ABC, abstractmethod
class Report(ABC):
    def display_report_info(self):
        print("This is a report.")

    @abstractmethod
    def generate(self):
        pass
class leads(Report):
    def generate(self):
        print("Generating leads report.")
class projects(Report):
    def generate(self):
        print("Generating projects report.")
class prograss(Report):
    def generate(self):
        print("Generating prograss report.")
leads().generate()
projects().generate()
prograss().generate()