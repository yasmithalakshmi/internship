# Level 2: HAS-A Relationship - Question 2
# Create a Computer class that HAS-A CPU object

class CPU:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cores = cores
    
    def info(self):
        print(f"CPU: {self.brand}, Cores: {self.cores}")


class Computer:
    def __init__(self, model, cpu):
        self.model = model
        self.cpu = cpu
    
    def display(self):
        print(f"Computer: {self.model}")
        self.cpu.info()


# Example usage
cpu = CPU("Intel i7", 8)
computer = Computer("Dell XPS", cpu)
computer.display()
