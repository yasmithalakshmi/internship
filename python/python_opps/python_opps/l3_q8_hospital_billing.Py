# Level 3: USES-A Relationship - Question 8
# Create a Hospital and BillingService class

class BillingService:
    def generate_bill(self, patient_name, amount):
        print(f"Bill generated for: {patient_name}")
        print(f"Amount: ${amount}")
        print("Payment required!")


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.billing_service = BillingService()
    
    def bill_patient(self, patient_name, amount):
        print(f"Hospital: {self.hospital_name}")
        self.billing_service.generate_bill(patient_name, amount)


# Example usage
hospital = Hospital("City Hospital")
hospital.bill_patient("John", 5000)
