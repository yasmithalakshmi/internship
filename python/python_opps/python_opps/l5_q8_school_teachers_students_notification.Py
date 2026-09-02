# Level 5: Combined Relationships - Question 8
# School HAS-A Teachers and Students, USES-A NotificationService

class Teacher:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name):
        self.name = name


class NotificationService:
    def notify(self, message):
        print(f"Notification: {message}")


class School:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.notification_service = NotificationService()
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    
    def add_student(self, student):
        self.students.append(student)
    
    def send_announcement(self, message):
        self.notification_service.notify(message)


# Example usage
school = School()
school.add_teacher(Teacher("Mr. Smith"))
school.add_student(Student("Alice"))
school.send_announcement("School closed today!")
