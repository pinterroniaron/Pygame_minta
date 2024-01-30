import pygame
from cloud import * 
from level import Level
from settings import *

pygame.init()  # Initialize pygame
pygame.font.init()  # Initialize the font module

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
clouds_group = pygame.sprite.Group()
level = Level(level_map, screen, clouds_group)
font_colour = (0,0,0)

sky = (135,206,235)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Cloud.handle_click(event.pos, clouds_group)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                Cloud.counter = 0
                Cloud.last_counter = None
                clouds_group.empty()
                level = Level(level_map, screen, clouds_group)

    if Cloud.counter != Cloud.last_counter:
        game_font = pygame.font.Font(None, 60)
        text_surf = game_font.render(f'Felrobbantott felhők száma: {Cloud.counter}', True, font_colour)
        text_rect = text_surf.get_rect(center=(width/2, 50))
        Cloud.last_counter = Cloud.counter

    screen.fill(sky)
    level.run()
    screen.blit(text_surf, text_rect)
    pygame.display.update()    
    clock.tick(60)

pygame.quit()