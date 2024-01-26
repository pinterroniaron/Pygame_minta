import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/dirt.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Sand(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/sand.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Sand_top(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/sand_top.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Grass(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/grass.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
