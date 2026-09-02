# Level 2: HAS-A Relationship - Question 10
# Create a Hospital class that HAS-A multiple Doctor and Patient objects

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    
    def info(self):
        print(f"  Doctor: {self.name} ({self.specialization})")


class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease
    
    def info(self):
        print(f"  Patient: {self.name} ({self.disease})")


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.doctors = []
        self.patients = []
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
    
    def add_patient(self, patient):
        self.patients.append(patient)
    
    def display_info(self):
        print(f"Hospital: {self.hospital_name}")
        print("Doctors:")
        for doctor in self.doctors:
            doctor.info()
        print("Patients:")
        for patient in self.patients:
            patient.info()


# Example usage
hospital = Hospital("City Hospital")
hospital.add_doctor(Doctor("Dr. Smith", "Cardiology"))
hospital.add_doctor(Doctor("Dr. Jane", "Neurology"))
hospital.add_patient(Patient("Alice", "Heart Disease"))
hospital.add_patient(Patient("Bob", "Migraine"))
hospital.display_info()
