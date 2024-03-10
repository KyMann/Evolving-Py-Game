import random
import Creature


def simulate(startingCreatures, generationsMax):
    simulateTime = 0
    allCreatures = []

    #make initail creatures
    for i in range(startingCreatures):
        allCreatures.append(Creature.creature(parent=''))

    #run the simulation loop
    while len(allCreatures) > 0 and simulateTime < generationsMax:
        print('tick ', simulateTime)
        cleanup = []
        #creatures do their live function
        for creature in allCreatures:
            print(creature)
            creature.live()
            if creature.dead:
                cleanup.append(creature)
        #remove outside of live loop
        for creature in cleanup:
            allCreatures.remove(creature)    
        
        simulateTime += 1
    
    #display    
    print('surviving:')
    for creature in allCreatures:
        print(creature)

if __name__ == '__main__':
    simulate(10, 9)