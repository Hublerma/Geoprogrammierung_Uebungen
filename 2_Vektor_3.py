#Aufgabe1

class Vector3:
    def __init__(self,x=0 ,y=0 ,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    
    def __add__(self, other): #Addieren nur wenn erster Komponent Vector3 ist  
        if type(other) == int or type(other) == float:
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other):
        return Vector3(self.x + other, self.y + other, self.z + other) #Addieren wenn der erste Komponent int oder float ist

    def __sub__(self, other): #Subtrahieren nur wenn erster Komponent Vector3 ist  
        if type(other) == int or type(other) == float:
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def __rsub__(self, other): #Subtrahieren wenn der erste Komponent int oder float ist
        return Vector3(self.x - other, self.y - other, self.z - other)
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector3(self.x * other, self.y * other, self.z * other) #Multiplikation mit Skalar als zweite Komponente
        else:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z) # komponentenweise Multiplikation 
        
    def __rmul__(self, other): #Multiplikation mit Skalar als erste Komponente
        return Vector3(self.x * other, self.y * other, self.z * other)
    
    def cross(self, other): #Kreuzprodukt des Vektors
        return Vector3(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    
    def dot(self, other): #Skalarprodukt des Vektor
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self): #Länge des Vektors als Hilfsgrösse für Normierung
        return float((self.x**2 + self.y**2 + self.z**2)**0.5)
    
    def normalize(self): #Normierung des Vektors
        length = self.length()
        if length == 0:
            print("Vektor mit Länge null kann nicht normiert werden.")
        else:
            return Vector3(self.x / length , self.y / length, self.z / length)

    
    
   
        
    
V1 = Vector3(1,2,3)
V2 = Vector3(-3,-2,-1)

print(V1) #Test __str__7

V3 = V1 + V2 #Test __add__
print(V3)
V4 = V1 + 1
print(V4)

V5 = 1 + V1 #Test __radd__
print(V5)

V6 = V2 - V1 #Test __sub__
print(V6)

V7 = V1 * V2 #Test __mul__
print(V7)
V8 = V1 * 2 #mit skalar
print(V8)

V9 = 2.5 * V1 #Test __rmul__
print(V9)

V10 = V1.cross(V2) #Test cross (Kreuzprodukt)
print(V10)

V11 = V1.dot(V2) #Test dot (Skalarprodukt)
print(V11)

V12 = V1.normalize() #Test normalize (Normierung)
print(V12)
print(V12.length())
V13 = Vector3(0,0,0)
print(V13.normalize())


    
