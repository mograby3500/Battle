import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.dmg = dmg
        self.cost = cost
        self.type = type

    def generate_dmg(self):
        low = self.dmg - 50
        high = self.dmg + 50
        return  random.randrange(low, high)


