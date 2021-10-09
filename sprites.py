import pygame

class Arrow(pygame.sprite.Sprite):

    def __init__(self, image, x, y, name) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect()
        self.name = name

    def collidepoint(self, pos) -> bool:
        return pos[0] > self.x and pos[0] < self.x + self.rect.size[0] and pos[1] > self.y and pos[1] < self.y + self.rect.size[1]
