# abstract HospitalEmployee class and implement Doctor, Nurse, and Pharmacist classes.
from abc import ABC, abstractmethod
class HospitalEmployee(ABC):
    @abstractmethod
    def work(self):
        pass
class Doctor(HospitalEmployee):
    def work(self):
        print("Doctor is diagnosing and treating patients.")

class Nurse(HospitalEmployee):
    def work(self):
        print("Nurse is assisting doctors and providing patient care.")

class Pharmacist(HospitalEmployee):
    def work(self):
        print("Pharmacist is compounding and dispensing medications.")
doctor = Doctor()
nurse = Nurse()
pharmacist = Pharmacist()

doctor.work()
nurse.work()
pharmacist.work()