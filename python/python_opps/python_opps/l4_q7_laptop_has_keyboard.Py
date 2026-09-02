# Level 4: Identify the Relationship - Question 7
# A Laptop has a Keyboard - HAS-A Relationship (Composition)

class Keyboard:
    def type(self, text):
        print(f"Typing: {text}")


class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()
    
    def use_keyboard(self, text):
        self.keyboard.type(text)


# Example usage
laptop = Laptop()
laptop.use_keyboard("Hello World")
