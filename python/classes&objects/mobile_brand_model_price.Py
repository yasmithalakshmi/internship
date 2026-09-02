# 4. Create a class called Mobile with properties for brand, model, and price. Create an object and display the values.

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

m = Mobile("Samsung", "Galaxy M32", 18000)
print("Brand:", m.brand)
print("Model:", m.model)
print("Price:", m.price)
