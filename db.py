class Money:
    def __init__(self):
        self.money = 0.0
        try:
            with open("money.txt", "r", newline="") as file:
                self.money = float(file.readline())
                
        except FileNotFoundError:
            with open("money.txt", "w") as file:
                self.money = 100.0
            
        

    def getMoney(self):
        return self.money
