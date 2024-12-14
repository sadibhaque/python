class shop:
    global_cart = [] # global attribute 
    def __init__(self, name):
        self.cart = [] # instanec attribute
        self.name = name
    
    def addCart(self, item):
        self.cart.append(item)



c1 = shop("Mendax")
c1.addCart("sdfsdd")

print(c1.name, c1.cart)