import random

class Mutation:
    def __init__(self, name, attribute, methodArray, repeatStyle):
        self.name = name
        self.attribute = attribute
        self.method = methodArray
        self.repeat = repeatStyle
    
    def __str__(self):
        return self.name

class Mutations:
    mutations =[
    Mutation(
        "photosynthesize",
        ["photosynthesisEnergy = 1"],
        ["def metabolize(self):",
         "     {}.metabolise(self)",
         "     self.energy += 1"
        ],
        "addAttribute"
        ),

    Mutation(
        "Size",
        ["MaxEnergy += 1", "MaxHealth += 1"],
        [""],
        "addAttribute"
        )
        ]

    def getMutation():
        mutation = random.choice(Mutations.mutations)
        return mutation

if __name__ == '__main__':
    print(Mutations.getMutation())