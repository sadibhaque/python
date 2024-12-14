class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []


class Driver:
    def __init__(self, name, license, age):
        self.license = license
        self.name = name
        self.age = age

class Counter:
    def __init__(self, address):
        pass

class Passenger:
    pass

class Supervisor:
    pass

