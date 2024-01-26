import pygame, sys

from level import Level
from settings import *

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

sky = (135,206,235)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(sky)

    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
