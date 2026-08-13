# abstract Course class with an abstract method start() and a normal method display_course_details().
from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def display_course_details(self):
        print(f"Course Name: {self.course_name}, Course Code: {self.course_code}")

    @abstractmethod
    def start(self):
        pass
class webDevelopment(Course):
    def start(self):
        print(f"Starting the web development course: {self.course_name}")
class DataScience(Course):
    def start(self):
        print(f"Starting the data science course: {self.course_name}")
class MachineLearning(Course):
    def start(self):
        print(f"Starting the machine learning course: {self.course_name}")
web_dev=webDevelopment("Web Development", "WD101")
data_science=DataScience("Data Science", "DS101")
ml=MachineLearning("Machine Learning", "ML101")
web_dev.display_course_details()
web_dev.start()
data_science.display_course_details()
data_science.start()
ml.display_course_details()
ml.start()