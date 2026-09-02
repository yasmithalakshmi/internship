# Level 3: USES-A Relationship - Question 10
# Create a Course and CertificateGenerator class

class CertificateGenerator:
    def generate_certificate(self, student_name, course_name):
        print(f"Generating certificate for: {student_name}")
        print(f"Course: {course_name}")
        print("Certificate generated successfully!")


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.certificate_generator = CertificateGenerator()
    
    def complete_course(self, student_name):
        print(f"Course: {self.course_name} - {student_name} completed!")
        self.certificate_generator.generate_certificate(student_name, self.course_name)


# Example usage
course = Course("Python Programming")
course.complete_course("Alice")
