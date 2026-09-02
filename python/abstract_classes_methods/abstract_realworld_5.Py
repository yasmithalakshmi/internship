#  abstract Transport class and implement Bus, Train, Flight, and Cab transportation.
from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def transport_details(self):
        pass
class Bus(Transport):
    def transport_details(self):
        print("Bus is a road vehicle for public transport.")
class Train(Transport):
    def transport_details(self):
        print("Train is a rail vehicle for long-distance travel.")
class Flight(Transport):
    def transport_details(self):
        print("Flight is an aircraft for air travel.")
class Cab(Transport):
    def transport_details(self):
        print("Cab is a car for private or shared transportation.")

Bus().transport_details()
Train().transport_details()
Flight().transport_details()
Cab().transport_details()