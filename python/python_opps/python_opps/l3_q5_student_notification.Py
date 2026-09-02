# Level 3: USES-A Relationship - Question 5
# Create a Student and NotificationService class

class NotificationService:
    def send_notification(self, message):
        print(f"Notification sent: {message}")


class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.notification_service = NotificationService()
    
    def notify_student(self, message):
        full_message = f"Hello {self.name}, {message}"
        self.notification_service.send_notification(full_message)


# Example usage
student = Student("Alice", "alice@example.com")
student.notify_student("Your assignment is due tomorrow!")
