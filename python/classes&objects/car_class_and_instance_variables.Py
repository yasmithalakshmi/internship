# 9. Create a Car class with class variables company and number_of_wheels, and instance variables model and price.

class Car:
    company = "Toyota"
    number_of_wheels = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

c1 = Car("Corolla", 1800000)
c2 = Car("Innova", 2200000)

print(c1.model, c1.price, Car.company, Car.number_of_wheels)
print(c2.model, c2.price, Car.company, Car.number_of_wheels)
