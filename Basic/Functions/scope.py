balance = 3000  # global scope

def buy (price) :
    global balance
    print(f"Before buy : {balance}")
    balance -= price
    print(f"After buy : {balance}")


buy(300)