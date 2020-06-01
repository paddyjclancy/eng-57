from class_animal import *

class Dog(Animal):
    def __init__(self, age, name = 'Un-named member', fur = "", independence = "", playful = ""):
        self.name = name.title()
        self.legs = 4
        self.age = int(age)
        self.fur = True
        self.independence = False
        self.playful = True
        self.family = "Canine"

    def bark(self):
        if self.name == "Freddie":
            return self.name + ":        Ayyyyyyyyyyyyyyyo!"
        else:
            return self.name + ":        WOOF!! WOOF!!"

    def fetch(self):
        if self.playful:
            return self.name + " chases a frisbee, and returns a drumstick"
        else:
            return self.name + ":        Nope..."

    def eat(self):
        return self.name + ":        'Head in bowl'"
