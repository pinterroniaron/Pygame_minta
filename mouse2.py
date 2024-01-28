import pygame
import random

WIDTH = 1280
HEIGHT = 620

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

balloon_surf = pygame.image.load('graphics/shooting/target.png').convert_alpha()
balloons_rect = []
for _ in range(5):
    balloon_rect = balloon_surf.get_rect(center=
    (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
    balloons_rect.append(balloon_rect)

crosshair_surf = pygame.image.load('graphics/shooting/crosshair.png').convert_alpha()
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, balloon_rect in enumerate(balloons_rect):
                if balloon_rect.collidepoint(event.pos):
                    del balloons_rect[index]

    screen.fill((140, 137, 246))

    for balloon_rect in balloons_rect:
        screen.blit(balloon_surf, balloon_rect)
    screen.blit(crosshair_surf, crosshair_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()    