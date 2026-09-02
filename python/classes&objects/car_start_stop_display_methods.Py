# 7. Create a Car class with methods start(), stop(), and display_details().

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "started")

    def stop(self):
        print(self.brand, self.model, "stopped")

    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car = Car("Honda", "City")
car.start()
car.display_details()
car.stop()
