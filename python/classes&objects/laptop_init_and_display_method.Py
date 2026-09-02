# 9. Create a Laptop class using __init__() and a method to display complete specifications.

class Laptop:
    def __init__(self, brand, ram, storage, price):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Price:", self.price)

laptop = Laptop("HP", "16GB", "512GB", 60000)
laptop.display()
