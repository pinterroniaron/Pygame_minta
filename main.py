import pygame

from level import Level
from settings import *

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")

    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
