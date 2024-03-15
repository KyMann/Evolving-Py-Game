import pygame
import Creature

WIDTH, HEIGHT = 1000, 1000

def game(entities):
    pygame.init()

    screen  = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Evolution Simulator")

    # entityGraphicalObjects = []
    # for entity in entities:
    #     entityGraphicalObjects.append(createEntity(pygame, entity))

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((117,98,27))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #screen.fill((0,0,0))
        
        screen.blit(background, (0,0))
        for entity in entities:
            drawCircle(pygame, screen, entity.color, entity.pos, entity.size)

        pygame.display.flip()
    pygame.quit()

def drawCircle(pygameObject, gameScreen, color, pos, size):
    pygameObject.draw.circle(gameScreen, color, pos, size)

# def createEntity(pygameObject, entity):
#     player = pygameObject.Surface((50, 50))
#     player.fill((255,255,0))
    
#     return player

if __name__ == '__main__':
    testCreatures = [
        Creature.Creature(parent='')
    ]
    game(testCreatures)