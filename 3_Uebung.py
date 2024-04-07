import math

class Figur:
    def __init__(self):
        self.name = "Figur"
    def Umfang(self):
        return 0
    def __str__(self):
        return self.name

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distanz(self, other):
         return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def __str__(self):
        return f"({self.x},{self.y})"


class Dreieck(Figur):
    def __init__(self, punkt_a, punkt_b, punkt_c):
        super().__init__()
        self.name = "Dreieck"
        self.a = punkt_a
        self.b = punkt_b
        self.c = punkt_c

    def Umfang(self):
        return self.a.distanz(self.b) + self.b.distanz(self.c) + self.c.distanz(self.a)
    
    def __str__(self):
        return f"{self.name} A{self.a}, B{self.b}, C{self.c}"

    

class Rechteck(Figur):
    def __init__(self, punkt_a, punkt_b):
        super().__init__()
        self.name = "Rechteck"
        self.a = punkt_a
        self.b = punkt_b
    
    def Umfang(self):
        return 2*abs(self.a.x - self.b.x) + 2*abs(self.a.y - self.b.y)
    
    def __str__(self):
        return f"{self.name} {self.a} - {self.b}"


class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__()
        self.name = "Kreis"
        self.m = mittelpunkt
        self.r = radius

    def Umfang(self):
        return self.r * 2 * math.pi
    
    def __str__(self):
        return f"{self.name} M={self.m} r={self.r}"


class Polygon(Figur):
    def __init__(self, *punkte):
        super().__init__()
        self.name = "Polygon"
        self.punkte = list(punkte)
    
    def Umfang(self):
        umfang = 0
        for i in range(len(self.punkte)):
            punkt_i = self.punkte[i]
            naechster_punkt = self.punkte[(i + 1) % len(self.punkte)]  
            umfang += punkt_i.distanz(naechster_punkt)
        return umfang
    
    def __str__(self):
        punkte = []
        for i in range(len(self.punkte)):
            punkte.append(str(self.punkte[i]))
        
        return f"{self.name} {punkte}"

Testdreieck = Dreieck(Point(0,0), Point(1,0.5), Point(0,1))
print(Testdreieck.Umfang())
print(Testdreieck)

Testrechteck = Rechteck(Point(0,0), Point(-5,-5))
print(Testrechteck.Umfang())
print(Testrechteck)

Testkreis = Kreis(Point(0,0), 10)
print(Testkreis.Umfang())
print(Testkreis)

Testpolygon4 = Polygon(Point(0,0), Point(1,0), Point(1,1), Point(0,1))
print(Testpolygon4.Umfang())
print(Testpolygon4)