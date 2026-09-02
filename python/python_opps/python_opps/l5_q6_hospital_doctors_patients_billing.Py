# Level 5: Combined Relationships - Question 6
# Hospital HAS-A Doctors and Patients, USES-A BillingService

class Doctor:
    def __init__(self, name):
        self.name = name


class Patient:
    def __init__(self, name):
        self.name = name


class BillingService:
    def bill(self, amount):
        print(f"Billing: ${amount}")


class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.billing_service = BillingService()
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def treat_patient(self):
        self.billing_service.bill(5000)


# Example usage
hospital = Hospital()
hospital.add_doctor(Doctor("Dr. Smith"))
hospital.add_patient(Patient("John"))
hospital.treat_patient()
