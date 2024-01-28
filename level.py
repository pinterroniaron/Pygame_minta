import pygame
from cloud import *
from player import Player
from settings import *
from tiles import *


class Level:
    def __init__(self, level_data, surface, clouds_group):
        self.display_surface = surface
        self.setup_level(level_data)
        self.clouds_group = clouds_group

        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                if cell == "X":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "T":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = Sand_top((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "S":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = Sand((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "G":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = Grass((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "F":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = Snow_dirt((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "H":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = Snow((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "M":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = melting_snow((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "W":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = water((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "B":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = water_bottom((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "D":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = melting_dirt((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "g":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile = melting_grass((x, y), tile_size)
                    self.tiles.add(tile)


    def run(self):
        Cloud.random_cloud(self.clouds_group, width, height)#random felhő generálás
        self.clouds_group.update(self.scroll_x()) #felhő update
        self.clouds_group.draw(self.display_surface) #felhő rajzolás
        Cloud.remove_offscreen_clouds(self.clouds_group)# kitörli a már nem képernyőn lévő felhőket

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()



    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > width - (width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

        return self.world_shift

    def horizontal_movement_collision(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
