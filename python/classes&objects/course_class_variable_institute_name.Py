# 10. Create a Course class with a class variable institute_name and instance variables course_name and duration.

class Course:
    institute_name = "SkillHub"

    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

c1 = Course("Python", "3 months")
c2 = Course("Java", "4 months")

print(c1.course_name, c1.duration, Course.institute_name)
print(c2.course_name, c2.duration, Course.institute_name)
