import random
import pygame


class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 2  #Felhő sebesség
    @staticmethod
    def random_cloud(group, width, height):
        cloud_image = pygame.image.load("graphics/map/clouds/cloud_1.png").convert_alpha()

        if random.randint(0, 100) < 2:  #Felhő esély
            new_cloud = Cloud(cloud_image, width, random.randint(0, height-500))
            group.add(new_cloud)

    @staticmethod
    def remove_offscreen_clouds(group):
        for cloud in group.copy():
            if cloud.rect.right < 0:
                group.remove(cloud)
    @staticmethod
    def handle_click(pos, group):
        for cloud in group:
            if cloud.rect.collidepoint(pos):
                group.remove(cloud)
                break

#problémák:
                #-a felhők a játékos és a blokkok eéőtt vanna
                #-ha mozog a kamera, akkor a felhők is mozognak fele együtt
                #-meg kell csinálni, hogy több felhő is generálódjon
                #-a felhő hitbox-a négyzet alakú nem pedig a felhő alakja
                #-el kell dönteni, hogy mikor generálódik pont elég felhő
                #-el kell dönteni, hogy milyen magasságban generálódjanak a felhők
                #-el kell dönteni, hogy mekkorák legyenek a felhők

