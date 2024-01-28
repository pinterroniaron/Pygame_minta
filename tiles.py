import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/dirt.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift: int):
        self.rect.x += x_shift

class Sand(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/sand.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift: int):
        self.rect.x += x_shift

class Sand_top(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/sand_top.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift: int):
        self.rect.x += x_shift

class Grass(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/grass.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift: int):
        self.rect.x += x_shift

class Snow_dirt(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/snow_dirt.png")
        self.rect = self.image.get_rect(topleft=pos)



    def update(self, x_shift: int):
        self.rect.x += x_shift

class Snow(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/snow.png")
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift: int):
        self.rect.x += x_shift
class melting_snow(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/melting_snow.png")
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift: int):
        self.rect.x += x_shift    
class water(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/water.png")
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift: int):
        self.rect.x += x_shift   
class water_bottom(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/water_bottom.png")
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift: int):
        self.rect.x += x_shift

class melting_dirt(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/melting_dirt.png")
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift: int):
        self.rect.x += x_shift

class melting_grass(pygame.sprite.Sprite):
    def __init__(self, pos: int, size: int):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/melting_grass.png")
        self.rect = self.image.get_rect(topleft=pos)
    def update(self, x_shift: int):
        self.rect.x += x_shift
