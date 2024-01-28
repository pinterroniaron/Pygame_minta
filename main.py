import pygame
from cloud import *
from level import Level
from settings import *

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
clouds_group = pygame.sprite.Group()
level = Level(level_map, screen, clouds_group)




sky = (135,206,235)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Cloud.handle_click(event.pos, clouds_group)


    screen.fill(sky)



    level.run()


    pygame.display.update()
    clock.tick(60)

pygame.quit()
