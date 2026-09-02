# 10. Create a HospitalPatient class using __init__() and a method to display patient information.

class HospitalPatient:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

    def display(self):
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Doctor:", self.doctor_name)

p = HospitalPatient("Harish", 32, "Asthma", "Dr. Pawan")
p.display()
