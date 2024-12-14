class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def move(self):
        pass

    def __repr__(self):
        return f"name : {self.name}\nprice : {self.price}"

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        super().__init__(name, price)

class Pickup(Truck):
    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)

class AcBus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self):
        return super().__repr__()


b1 = AcBus("Gree nLine", 1000000, 40, 30)

print(b1)

print()

print(b1.name, b1.temperature)