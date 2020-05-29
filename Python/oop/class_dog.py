
# Create class
class Dog:
    def __init__(self, name = 'Un-named member'):
        self.name = name.title()            # <-- Polymorphism
        self.legs = 4
        self.fur = True
        self.independence = False
        self.playful = True
        self.family = "Canine"

    def bark(self):
        return self.name + ":        WOOF!! WOOF!!"

    def nap(self):
        return self.name + ":        zZz... zZz..."

    def fetch(self):
        if self.playful:
            return self.name + " chases a frisbee, and returns a tree branch"
        else:
            return self.name + ":        Nope..."

    def eat(self):
        return self.name + ":        'Head in bowl'"

    def walk(self, independence):
        if self.independence:
            return self.name + ":        'Don't even think about it'"
        else:
            return self.name + " scratches the front door"
