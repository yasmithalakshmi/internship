#abstract Notification class with an abstract method send() and a normal method display_message().
from abc import ABC, abstractmethod
class Notification(ABC):
    def display_message(self):
        print("This is a notification.")

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
email.display_message()
email.send("Hello yasmitha!")
sms.display_message()
sms.send("Hello yashu!")