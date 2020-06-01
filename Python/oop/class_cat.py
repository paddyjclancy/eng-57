from class_animal import *


class Cat(Animal):

    def __init__(self, name, age, independence="", playful="", agility=""):
        super().__init__("Feline", 4, True)
        self.name = name.title()
        self.__age = int(age)
        self.independence = True
        self.playful = True
        self.agility = True

    def purr(self):
        return self.name + ":        Prrrrrrrrrrrrrprrrrrrrrrrr"

    def catnip(self):
        return self.name + ":       （Φ ω Φ） 'I am the Voodoo Child'  （Φ ω Φ）"

    def alarm(self):
        return self.name + " knocks a picture frame off bedside table"

    def eat(self):
        return f"Today {self.name} gets tuna"

    def getter_age(self):                   # Getter method (Encapsulation)
        return self.__age

    def birthday(self):
        print(f"It is your birthday, {self.name}.")
        self.__age_increase()               # Encapsulated method
        print(f"{self.name} is now {self.__age} years old.")

    def __age_increase(self):               # Setter method (Encapsulation)
        self.__age += 1
