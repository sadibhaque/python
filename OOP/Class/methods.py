class Phone:
    price = 100
    color = 'Black'
    brand = 'Apple'
    features = ['Camera', 'Speaker', 'Wifi']

    def call(self):
        print("Calling One Person !")
    
    def sms(self, num,msg):
        return f"Sending this {msg} to this number {num}."


p1 = Phone()
print(p1.features)
p1.call()
ans = p1.sms(171,"Hi")
print(ans)