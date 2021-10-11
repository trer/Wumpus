import pygame
from game.game import Map
from sprites import Sprite

pygame.init()
map = Map()

pygame.display.set_caption("Wumpus")
icon = pygame.image.load('images/monster.png')

pygame.display.set_icon(icon)

wumpus = pygame.image.load('images/Wumpus.PNG')
wumpus = pygame.transform.scale(wumpus, (64, 64))

stench = pygame.image.load('images/stench.jpg')
stench = pygame.transform.scale(stench, (64, 64))

hero = pygame.image.load('images/hero.jpg')
hero = pygame.transform.scale(hero, (64, 64))

gold = pygame.image.load('images/gold.jpeg')
gold = pygame.transform.scale(gold, (64, 64))

arrow = pygame.image.load('images/arrow.jpg')
arrow_right = pygame.transform.scale(arrow, (100, 50))
arrow_up = pygame.transform.rotate(arrow_right, 90)
arrow_left = pygame.transform.rotate(arrow_up, 90)
arrow_down = pygame.transform.rotate(arrow_left, 90)

easy = Sprite(pygame.Surface((100, 50)), 250, 150, 'easy')
medium = Sprite(pygame.Surface((100, 50)), 250, 225, 'medium')
hard = Sprite(pygame.Surface((100, 50)), 250, 300, 'hard')

sprites = [Sprite(arrow_right, 675, 300, Map.RIGHT),
           Sprite(arrow_up, 600, 175, Map.UP),
           Sprite(arrow_left, 475, 300, Map.LEFT),
           Sprite(arrow_down, 600, 375, Map.DOWN),
           easy,
           medium,
           hard]

screen = pygame.display.set_mode((800, 600))


# TODO sprites for pit, breeze, and empty tile
# Do printing on screen and not to terminal

def draw_map():
    difficulty = map.difficulty
    screen.fill((128, 128, 128))
    screen.blit(arrow_right, (675, 300))
    screen.blit(arrow_up, (600, 175))
    screen.blit(arrow_left, (475, 300))
    screen.blit(arrow_down, (600, 375))
    size = 66
    for x in range(0, map.size):
        for y in range(0, map.size):
            type = map.map[x][y].type
            con = map.map[x][y].contains()
            do_draw = difficulty == 'easy' or \
                      (difficulty == 'medium' and map.visited[x][y]) or \
                      (difficulty == 'hard' and 'player' in con)
            drawed = False
            color = (34, 139, 34)
            if do_draw:
                if map.visited[x][y]:
                    color = (100, 100, 100)
                if 'wumpus' in type:
                    screen.blit(wumpus, (x * size, y * size))
                    drawed = True
                if 'stench' in con:
                    screen.blit(stench, (x * size, y * size))
                    drawed = True
                if 'player' in con:
                    screen.blit(hero, (x * size, y * size))
                    drawed = True
                if 'gold' in con:
                    screen.blit(gold, (x * size, y * size))
                    drawed = True
            if not drawed:

                pygame.draw.rect(screen, color, (x * size, y * size, size - 2, size - 2))


running = True
done = True


def start():
    global map, done, running
    while done:
        pos = pygame.mouse.get_pos()
        screen.fill((128, 128, 128))
        screen.blit(easy.image, (easy.x, easy.y))
        screen.blit(medium.image, (medium.x, medium.y))
        screen.blit(hard.image, (hard.x, hard.y))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_sprites = [s for s in sprites if s.collidepoint(pos)]
                for item in clicked_sprites:
                    if item.name == 'easy':
                        done = False
                        map.difficulty = 'easy'
                    if item.name == 'medium':
                        done = False
                        map.difficulty = 'medium'
                    if item.name == 'hard':
                        done = False
                        map.difficulty = 'hard'
            if event.type == pygame.QUIT:
                done = False
                running = False
        pygame.display.update()
    map.init()


start()

while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_sprites = [s for s in sprites if s.collidepoint(pos)]
            for item in clicked_sprites:
                if type(item) == Sprite:
                    result = map.move(item.name)
                    if result == Map.LOSS:
                        print("You lose")
                        done = True
                    elif result == Map.WIN:
                        print("You win")
                        done = True
                    elif type(result) == list:
                        if 'stench' in result:
                            print("you smell a terrible stench")
                        if 'gold' in result:
                            print("You find the gold, now you only have to find your way back.")

        if event.type == pygame.QUIT:
            running = False
    if done:
        start()
    draw_map()
    pygame.display.update()
