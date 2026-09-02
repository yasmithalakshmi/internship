# 10. Create a Hospital class with patient name, age, disease, and doctor name. Create three patient objects.

class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

p1 = Hospital("Arun", 28, "Fever", "Dr. Ghosh")
p2 = Hospital("Neha", 35, "Cold", "Dr. Singh")
p3 = Hospital("Ritu", 42, "Migraine", "Dr. Kapoor")

for patient in [p1, p2, p3]:
    print(patient.patient_name, patient.age, patient.disease, patient.doctor_name)
