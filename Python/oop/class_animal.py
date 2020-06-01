
class Animal():

    def walk(self, independence):
        if self.independence:
            return self.name + ":        'Don't even think about it'"
        else:
            return self.name + " scratches the front door"

    def nap(self):
        return self.name + ":        zZz... zZz..."