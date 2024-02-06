import sys

import pygame

WIDTH = 1280
HEIGHT = 620
SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
obstacle_colour = black
obstacle_colour_2 = black
kacsa = pygame.image.load("minta/kacsa.png").convert_alpha()
kacsa_rect = kacsa.get_rect(center=(WIDTH / 2, HEIGHT / 2))

running = True
while running:
    screen.fill((140, 150, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Irányítás egérrel
            kacsa_rect.center = event.pos

    # Irányítás billentyűzettel
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and kacsa_rect.right <= WIDTH:
        kacsa = pygame.image.load("minta/kacsaflip.png")
        kacsa_rect.x += SPEED
    elif keys[pygame.K_LEFT] and kacsa_rect.left >= 0:
        kacsa = pygame.image.load("minta/kacsa.png")
        kacsa_rect.x -= SPEED
    if keys[pygame.K_UP] and kacsa_rect.top >= 0:
        kacsa_rect.y -= SPEED
    elif keys[pygame.K_DOWN] and kacsa_rect.bottom <= HEIGHT:
        kacsa_rect.y += SPEED

    # Ütközés
    obstacle = pygame.draw.rect(screen, obstacle_colour, (100, 100, 200, 200))
    if kacsa_rect.colliderect(obstacle):
        obstacle_colour = red
    else:
        obstacle_colour = black

    obstacle_2 = pygame.draw.rect(
        screen, obstacle_colour_2, (WIDTH - 300, 100, 200, 200)
    )
    if kacsa_rect.colliderect(obstacle_2):
        obstacle_colour_2 = green
    else:
        obstacle_colour_2 = black

    screen.blit(kacsa, kacsa_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
