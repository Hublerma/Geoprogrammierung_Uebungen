## Komposition

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Strecke:
    def __init__(self,punkt1,punkt2):
        self.A = punkt1
        self.B = punkt2

A = Punkt(3,4)
B = Punkt(4,5)

s = Strecke(A,B)