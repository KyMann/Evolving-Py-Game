import random
import string

class creature:
    def __init__(self, parent ):
        
        if parent=='':
            self.dead = False
            self.EnergyMax = 10
            self.Energy = 10
            self.HitPointsMax = 10
            self.HitPoints = 10 #int
            self.Defense = 10 #nit
            self.Attack = 10 #int
            self.name = ''.join(random.choice(string.ascii_lowercase))
        else:
            self.dead = False
            self.EnergyMax = parent.EnergyMax
            self.Energy = 10
            self.HitPointsMax = parent.HitPointsMax
            self.HitPoints = parent.HitPointsMax
            self.Defense = parent.Defense
            self.Attack = parent.Attack
            self.name = parent.name.join(random.choice(string.ascii_lowercase))
        self.age = 0

    def live(self):
        self.metabolize()

    def metabolize(self):
        self.Energy -= 1
        if self.Energy <= 0:
            self.dead = True
        self.age += 1
    
    def mutate(self):
        pass

    def __str__(self):
        return "name:{} Energy:{}/{} Age:{}".format(self.name, self.Energy, self.EnergyMax, self.age)