from class_animal import *

class Cockroach(Animal):
    def __init__(self):
        self.legs = 6
        self.fur = False
        self.independence = True
        self.family = "Blattidae"

    def scurry(self):
        if self.legs > 6:
            return f"{self} scurries away slightly slower"
        else:
            return f"{self} scurries away under the workbench rapidly"
