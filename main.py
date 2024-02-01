from os import write
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
sky = (135, 206, 235)
running: bool = True
best = 1000000
best_time = 0
prev_time = 0

while running:
    time = (int(pygame.time.get_ticks() / 1000) - prev_time)

    with open("records.txt", "r", encoding="utf-8") as file:
        for line in file:
            number = int(line.strip())
            if number < best:
                best = number

    if best != 1000000:
        best_time = best


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
                prev_time += time
            elif event.key == pygame.K_t:
                with open("records.txt", "a", encoding="utf-8") as file:
                    file.write(f"{str(time)}\n")



    game_font: pygame.font.Font = pygame.font.Font(None, 60)
    text_surf_2: pygame.Surface = game_font.render(f'Idő: {time} másodperc', True, font_colour)
    text_rect_2: pygame.Rect = text_surf_2.get_rect(center=(1500, 50))

    game_font: pygame.font.Font = pygame.font.Font(None, 60)
    text_surf_3: pygame.Surface = game_font.render(f'Legjobb idő: {best_time} másodperc', True, font_colour)
    text_rect_3: pygame.Rect = text_surf_2.get_rect(center=(1500, 100))


    if Cloud.counter != Cloud.last_counter:
        game_font: pygame.font.Font = pygame.font.Font(None, 60)
        text_surf: pygame.Surface = game_font.render(f'Felrobbantott felhők száma: {Cloud.counter}', True, font_colour)
        text_rect: pygame.Rect = text_surf.get_rect(center=(400, 50))
        Cloud.last_counter = Cloud.counter


    screen.fill(sky)
    level.run()
    screen.blit(text_surf, text_rect)
    screen.blit(text_surf_2, text_rect_2)
    screen.blit(text_surf_3, text_rect_3)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
