from class_animal import *

class Dog(Animal):

    def __init__(self, age, name = 'Un-named member', independence = "", playful = "", toy = ""):
        super().__init__("Canine", 4, True)
        self.name = name.title()
        self.__age = int(age)
        self.independence = False
        self.playful = True
        self.toy = "ball"

    def bark(self):
        if self.name == "Freddie":
            return self.name + ":        Ayyyyo!"
        else:
            return self.name + ":        WOOF!! WOOF!!"

    def fetch(self, toy):
        if self.playful:
            return f"{self.name} chases the {toy}"
        else:
            return self.name + ":        Nope..."

