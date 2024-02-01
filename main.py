import pygame
from cloud import Cloud
from level import Level
from settings import width, height, level_map

pygame.init()
pygame.font.init()

screen: pygame.Surface = pygame.display.set_mode((width, height))
clock: pygame.time.Clock = pygame.time.Clock()
clouds_group: pygame.sprite.Group = pygame.sprite.Group()
level: Level = Level(level_map, screen, clouds_group)

font_colour = (0, 0, 0)
time_prev = None
sky = (135, 206, 235)


running: bool = True
while running:
    time = pygame.time.get_ticks()
    print(int(time / 1000))
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
        game_font: pygame.font.Font = pygame.font.Font(None, 60)
        text_surf: pygame.Surface = game_font.render(f'Felrobbantott felhők száma: {Cloud.counter}', True, font_colour)
        text_rect: pygame.Rect = text_surf.get_rect(center=(400, 50))
        Cloud.last_counter = Cloud.counter

    for e in range(60):
        if e == 60:
            time += 1
            time_prev = time
    

    screen.fill(sky)
    level.run()
    screen.blit(text_surf, text_rect)
    pygame.display.update()    
    clock.tick(60)

pygame.quit()
