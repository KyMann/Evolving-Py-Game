import random
import string
import numpy as np
import Mutations

class Creature:
    def __init__(self, parent ):
        if parent=='':
            self.dead = False
            self.EnergyMax = 10
            self.Energy = 4
            self.HitPointsMax = 10
            self.HitPoints = 10 
            self.name = ''.join(random.choice(string.ascii_lowercase))
            self.reproduceRate = 1
            self.mutations = []
        else:
            self.dead = False
            self.EnergyMax = parent.EnergyMax
            self.Energy = 10
            self.HitPointsMax = parent.HitPointsMax
            self.HitPoints = parent.HitPointsMax
            self.name = parent.name+''.join(random.choice(string.ascii_lowercase))
            self.reproduceRate = parent.reproduceRate
            self.mutations = parent.mutations
        self.age = 0
        

    def live(self, world):
        self.metabolize()
        self.reproduce(world)

    def metabolize(self):
        self.Energy -= 1
        if self.Energy <= 0:
            self.dead = True
        self.age += 1
    
    def reproduce(self, world):
        child = Creature(self)
        child.mutate()
        world.append(child) #TODO - make child of new class

    def getSpecies(self):
        return __name__

    def __str__(self):
        return "name:{} Species:{} Energy:{}/{} Age:{}".format(self.name, self.getSpecies(), self.Energy, self.EnergyMax, self.age)
    
    def mutate(self):
        newCreature = self.name+''.join(random.choice(string.ascii_lowercase))
        newTrait = []
        newMethod = []
        if np.random.normal() > .89: #100-N = percent chance that we'll mutate
            mutation = Mutations.Mutations.getMutation()
            if mutation not in self.mutations:
            
                self.mutations.append(mutation.name)    
            
                #put traits into traits section    
                newTrait = mutation.attribute 
                #put methods into methods section
                for method in mutation.method:
                    newMethod.append(method.format(self.getSpecies()))
            #TODO: make mutations enter new class
            else:
                match mutation.repeatStyle:
                    case "addAttribute":
                        pass
        Lines = [
            "import random \n",
            "import string \n",
            "import numpy as np \n",
            "import Mutations \n",
            "\n",
            "class {}({}): \n".format(newCreature, self.getSpecies()),
            "     def __init__(self, parent): \n",
            "          {}.__init__(self, parent) \n".format(self.getSpecies()),
            "\n"
            ] + newTrait + ["\n"] + newMethod
        newCreatureFileName = 'creatures/' + newCreature + '.py'
        with open(newCreatureFileName, 'w') as f:
            f.writelines(Lines)
        
        return 