# 4. Create a Car class using __init__() and methods start(), stop(), and display().

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(self.brand, self.model, "started")

    def stop(self):
        print(self.brand, self.model, "stopped")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car = Car("Ford", "EcoSport")
car.start()
car.display()
car.stop()
