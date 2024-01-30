import pygame

from cloud import Cloud
from player import Player
from settings import height, tile_size, width
from tiles import (
    Grass,
    Sand,
    Sand_top,
    Snow,
    Snow_dirt,
    Tile,
    melting_dirt,
    melting_grass,
    melting_snow,
    water,
    water_bottom,
)


class Level:
    def __init__(self, level_data: list, surface: pygame.Surface, clouds_group):
        self.display_surface: pygame.Surface = surface
        self.setup_level(level_data)
        self.clouds_group = clouds_group
        self.world_shift: int = 0

    def setup_level(self, layout: list) -> None:
        self.tiles: pygame.sprite.Group[Tile] = pygame.sprite.Group()
        self.player: pygame.sprite.GroupSingle[Player] = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                if cell == "X":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: Tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "P":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    player_sprite: Player = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "T":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: Sand_top = Sand_top((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "S":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: Sand = Sand((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "G":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: Grass = Grass((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "F":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: Snow_dirt = Snow_dirt((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "H":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: Snow = Snow((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "M":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: melting_snow = melting_snow((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "W":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: water = water((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "B":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: water_bottom = water_bottom((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "D":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: melting_dirt = melting_dirt((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == "g":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile: melting_grass = melting_grass((x, y), tile_size)
                    self.tiles.add(tile)

    def run(self) -> None:
        Cloud.random_cloud(self.clouds_group, width, height)  # random felhő generálás
        self.clouds_group.update(self.scroll_x())  # felhő update
        self.clouds_group.draw(self.display_surface)  # felhő rajzolás
        Cloud.remove_offscreen_clouds(
            self.clouds_group
        )  # kitörli a már nem képernyőn lévő felhőket

        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.player.update()
        self.player.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()

    def scroll_x(self) -> int:
        player: Player = self.player.sprite
        player_x: int = player.rect.centerx
        direction_x: float = player.direction.x

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

    def horizontal_movement_collision(self) -> None:
        player: Player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self) -> None:
        player: Player = self.player.sprite
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
