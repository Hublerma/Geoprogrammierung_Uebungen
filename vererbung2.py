import math

class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figur:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def flaeche(self):
        return 0
    
    def schwerpunkt(self):
        pass

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.m = mittelpunkt
        self.r = radius
    
    def flaeche(self):
        return math.pi * self.r**2
    
        

k = Kreis(Punkt(0,0) , 10)
print(k.name, k.flaeche())
    
    