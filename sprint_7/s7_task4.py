class WashingMachine:
    
    def __init__(self):
        self.wash = Washing()
        self.rinse = Rinsing()
        self.spin = Spinning()
        self.startWashing()
        
    def startWashing(self):
        self.wash.wash()
        self.rinse.rinse()
        self.spin.spin()
    
class Washing:
    def wash(self):
        print('Washing...')
    
class Rinsing:
    def rinse(self):
        print('Rinsing...')

class Spinning:
    def spin(self):
        print('Spinning...')
