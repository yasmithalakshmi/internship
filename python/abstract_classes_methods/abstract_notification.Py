# abstract class Notification with an abstract method send(). Implement it using EmailNotification and SMSNotification.
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")
email=EmailNotification()
sms=SMSNotification()
email.send("Hello yasmitha!")
sms.send("Hello yashu!")