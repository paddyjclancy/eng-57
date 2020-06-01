
class Dog:
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

    def nap(self):
        return self.name + ":        zZz... zZz..."

    def fetch(self):
        if self.playful:
            return self.name + " chases a frisbee, and returns a drumstick"
        else:
            return self.name + ":        Nope..."

    def eat(self):
        return self.name + ":        'Head in bowl'"

    def walk(self, independence):
        if self.independence:
            return self.name + ":        'Don't even think about it'"
        else:
            return self.name + " scratches the front door"
