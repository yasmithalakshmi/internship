# Level 5: Combined Relationships - Question 2
# Person → Student (IS-A) and Student HAS-A Course

class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
    
    def display(self):
        print(f"Student: {self.name}, Course: {self.course.course_name}")


# Example usage
course = Course("Python Programming")
student = Student("Alice", course)
student.display()
