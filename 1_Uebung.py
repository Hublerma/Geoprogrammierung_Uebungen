#Aufgabe1

class Vektor3:
    def __init__(self,x=0 ,y=0 ,z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def __abs__(self):
        return Vektor3(abs(self.x), abs(self.y), abs(self.z))
    
    def __add__(self, other): #Funktioniert nur wenn esretr KOmponent Vektor ist  
        if type(other) == int or type(other) == float:
            return Vektor3(self.x + other, self.y + other, self.z + other)
        else:
            return Vektor3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other):
        return Vektor3(self.x + other, self.y + other, self.z + other) #addieren wenn der erste Komponent kein Vektor ist

    
    def __sub__(self, other):
        return Vektor3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    
    
V1 = Vektor3(1,1,1)
V2 = Vektor3()

print(V1)
print(V1.len())
print(V2.len())

V3 = V1 + V2


print(V3)

V5 = Vektor3(7,8,1)

V6 = 1 + V5
print(V6)


#---------------------------------------------------------------------

#Aufgabe 2

class WGS84Coord:
    def __init__(self, _longitude = 0, _latitude = 0):
        self.setCoordinates(_longitude, _latitude)
    
    def setCoordinates(self, _longitude, _latitude):
        if  _longitude < -180 or _longitude > 180:
            _longitude = (_longitude + 180) % 360 - 180
            print("Longitude ausserhalb [-180, 180] korrigiert")
        if _latitude > 90:
            _latitude = 90 - (_latitude - 90)
            print("Latitude > 90 korrigiert")
        elif _latitude < -90:
            _latitude = -90 - (_latitude + 90)
            print("Latitude < -90 korrigiert")
        self._longitude = _longitude
        self._latitude = _latitude

    def getCoordinates(self):
        return((self._longitude, self._latitude))
    
    coordinates = property(getCoordinates, setCoordinates)
    

Test = WGS84Coord(152,65) 

print(Test.coordinates)
    
Test = WGS84Coord(181,91)

print(Test.coordinates)

Test = WGS84Coord(-181,-91)

print(Test.coordinates)

Test_leer = WGS84Coord()

print(Test_leer.coordinates)