# use of __init__


class phone:
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price



p1 = phone("Mendax", "Apple", 1000000000)
p2 = phone("Carbine", "Sony", 2000000000)
p3 = phone("Drifter", "Pixel", 3000000000)

l = {p1,p2,p3}

for i in l:
    print(i.owner, i.brand, i.price)