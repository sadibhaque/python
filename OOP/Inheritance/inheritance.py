
# base class, parent class, common functionality class

class Device:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def run(self):
        return f"Running Device : {self.brand}"

class Laptop:
    def __init__(self, memory):
        self.memory = memory
    
    def coding(self):
        return f"Learning Python and practicing."
    

class Phone(Device):
    def __init__(self, brand, price, color, sim):
        super().__init__(brand, price, color)
        self.sim = sim
    
    def call(self, number):
        return f"Calling {self.number}"
    
    def __repr__(self):
        return f"This has Dual sim" if self.sim == True else "This has Single sim"
    


class Camera:
    def __init__(self, pixel):
        self.pixel = pixel


p1 = Phone("apple", 100000, 'red', True)
print(p1)
print(p1.brand,p1.price,p1.color)