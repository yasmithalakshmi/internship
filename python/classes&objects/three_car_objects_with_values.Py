# 4. Create a Car class with brand, model, year, and price. Create three objects with different values.

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

cars = [
    Car("Tesla", "Model 3", 2023, 4500000),
    Car("BMW", "X5", 2022, 7000000),
    Car("Audi", "A4", 2021, 5000000)
]

for car in cars:
    print(car.brand, car.model, car.year, car.price)
