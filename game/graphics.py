import pygame



pygame.init()

pygame.display.set_caption("Wumpus")
icon = pygame.image.load('game/monster.PNG')
pygame.display.set_icon(icon)


screen = pygame.display.set_mode((800, 600))

# TODO create map layout
# Hook up to backend
# spites for wumpus, player, pit, breeze, stench, gold and empty tile

running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,0,0))
    pygame.display.update()