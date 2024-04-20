## Komposition

class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Strecke:
    def __init__(self, x1, y1, x2, y2):
        self.A = Punkt(x1, y1)
        self.B = Punkt(x2, y2)

s = Strecke(1,2,3,4)