class Laptop:
    def __init__(self, brand, price, color, memory,):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
    def run(self):
        return f"Running Laptop : {self.brand}"
    
    def coding(self):
        return f"Learning Python and practicing."
    

class Phone:
    def __init__(self, brand, price, color, sim,):
        self.brand = brand
        self.price = price
        self.color = color
        self.sim = sim
    
    def call(self, number):
        return f"Calling {self.number}"
    


    