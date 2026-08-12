# abstract class Notification with abstract methods send() and schedule(). Implement them in Email, SMS, and WhatsApp.
from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def schedule(self, time):
        pass
class Email(Notification):
    def send(self, message):
        print(f"Sending email notification: {message}")

    def schedule(self, time):
        print(f"Scheduling email notification at {time}")
class SMS(Notification):
    def send(self, message):
        print(f"Sending SMS notification: {message}")

    def schedule(self, time):
        print(f"Scheduling SMS notification at {time}")
class WhatsApp(Notification):
    def send(self, message):
        print(f"Sending WhatsApp notification: {message}")

    def schedule(self, time):
        print(f"Scheduling WhatsApp notification at {time}")
email = Email()
sms = SMS()
whatsapp = WhatsApp()
email.send("Hello yasmitha!")
email.schedule("10:00 AM")
sms.send("Hello yashu!")
sms.schedule("11:00 AM")
whatsapp.send("Hello yasmitha!")
whatsapp.schedule("12:00 PM")