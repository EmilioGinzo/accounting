class account:
    name = ""
    balance = 0.0
    
    def __init__(self, name):
        self.name = name
    

account1 = account("Emilio")

print("balance: " + account1.name)

