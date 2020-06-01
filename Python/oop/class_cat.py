from class_animal import *

class Cat(Animal):
    def __init__(self, name, age, fur ="", independence = "", agility = "", playful = ""):
        self.name = name.title()
        self.legs = 4
        self.age = int(age)
        self.fur = True
        self.independence = True
        self.agility = True
        self.playful = True
        self.family = "Feline"

    def purr(self):
        return self.name + ":        Prrrrrrrrrrrrrprrrrrrrrrrr"

    def catnip(self):
        return self.name + ":       （Φ ω Φ） 'I am the Voodoo Child'  （Φ ω Φ）"

    def alarm(self):
        return self.name + " knocks a picture frame off bedside table"

