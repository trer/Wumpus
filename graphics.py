import pygame
from game.game import Map
from sprites import Arrow
map = Map()

pygame.init()

pygame.display.set_caption("Wumpus")
icon = pygame.image.load('game/monster.PNG')

pygame.display.set_icon(icon)

wumpus = pygame.image.load('game/Wumpus.PNG')
wumpus = pygame.transform.scale(wumpus, (64, 64))

stench = pygame.image.load('game/stench.jpg')
stench = pygame.transform.scale(stench, (64, 64))

hero = pygame.image.load('game/hero.jpg')
hero = pygame.transform.scale(hero, (64, 64))

gold = pygame.image.load('game/gold.jpeg')
gold = pygame.transform.scale(gold, (64, 64))

arrow = pygame.image.load('game/arrow.jpg')
arrow_right = pygame.transform.scale(arrow, (100, 50))
arrow_up = pygame.transform.rotate(arrow_right, 90)
arrow_left = pygame.transform.rotate(arrow_up, 90)
arrow_down = pygame.transform.rotate(arrow_left, 90)
sprites = [Arrow(arrow_right, 675, 300, Map.RIGHT),
           Arrow(arrow_up, 600, 175, Map.UP),
           Arrow(arrow_left, 475, 300, Map.LEFT),
           Arrow(arrow_down, 600, 375, Map.DOWN)]


screen = pygame.display.set_mode((800, 600))

screen.fill((128,128,128))
screen.blit(arrow_right, (675, 300))
screen.blit(arrow_up, (600, 175))
screen.blit(arrow_left, (475, 300))
screen.blit(arrow_down, (600, 375))


# TODO sprites for pit, breeze, and empty tile
# restart the game
# show results
# play blind

def draw_map():
    size = 66
    for x in range(0, map.size):
        for y in range(0, map.size):
            type = map.map[x][y].type
            con = map.map[x][y].contains()
            drawed = False
            if 'wumpus' in type:
                screen.blit(wumpus, (x*size, y*size))
                drawed = True
            if 'stench' in con:
                screen.blit(stench, (x*size, y*size))
                drawed = True
            if 'player' in con:
                screen.blit(hero, (x*size, y*size))
                drawed = True
            if 'gold' in con:
                screen.blit(gold, (x*size, y*size))
                drawed = True
            if not drawed:  
                pygame.draw.rect(screen, (34,139,34), (x*size, y*size, size-2, size-2))
    

running = True
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in sprites if s.collidepoint(pos)]
            if clicked_sprites:
                item = clicked_sprites[0]
                if type(item) == Arrow:
                    result = map.move(item.name)
                    if result == Map.LOSS:
                        print("You lose")
                    elif result == Map.WIN:
                        print("You win")
                    elif type(result) == list:
                        if 'stench' in result:
                            print("you smell a terrible stench")
                        if 'gold' in result:
                            print("You find the gold, now you only have to find your way back.")
            
        if event.type == pygame.QUIT:
            running = False

    draw_map()
    pygame.display.update()