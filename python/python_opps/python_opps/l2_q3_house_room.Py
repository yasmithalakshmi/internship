# Level 2: HAS-A Relationship - Question 3
# Create a House class that HAS-A Room objects

class Room:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def info(self):
        print(f"  Room: {self.name}, Size: {self.size} sqft")


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def display(self):
        print(f"House: {self.address}")
        print("Rooms:")
        for room in self.rooms:
            room.info()


# Example usage
house = House("123 Main Street")
house.add_room(Room("Bedroom", 200))
house.add_room(Room("Kitchen", 150))
house.add_room(Room("Bathroom", 100))
house.display()
