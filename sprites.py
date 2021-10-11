import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, x, y, name) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = image.get_rect()
        self.name = name
        if type(name) == str:
            self.font = pygame.font.SysFont('Arial', 25)
            self.image.blit(self.font.render(name, True, (255, 0, 0)), (0, 0))

    def collidepoint(self, pos) -> bool:
        return self.x < pos[0] < self.x + self.rect.size[0] and self.y < pos[1] < self.y + self.rect.size[1]
