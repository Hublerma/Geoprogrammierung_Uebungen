# Vererbung

class Tier:
    def __init__(self, name, anzahlBeine):
        self.name = name
        self.anzahlBeine = anzahlBeine
    
    def essen(self):
        print("mjam")
    
    def lautausgabe(self):
        print("????")
    

class Hund(Tier):
    def __init__(self):
        super().__init__("Hund", 4)

    def lautausgabe(self):
        print("wuff")

bello = Hund()

print(bello.anzahlBeine)
print(bello.name)
bello.essen()
bello.lautausgabe()