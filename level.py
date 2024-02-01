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
    def __init__(
        self, level_data: list[str], surface: pygame.Surface, clouds_group: None
    ):
        self.display_surface: pygame.Surface = surface
        self.tiles_dict = {}
        self.setup_level(level_data)
        self.clouds_group = clouds_group
        self.world_shift: int = 0

    def setup_level(self, layout: list[str]) -> None:
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                if cell == "X":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_X: Tile = Tile((x, y))
                    self.tiles.add(tile_X)
                if cell == "P":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    player_sprite: Player = Player((x, y))
                    self.player.add(player_sprite)
                if cell == "T":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_T: Sand_top = Sand_top((x, y))
                    self.tiles.add(tile_T)
                if cell == "S":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_S: Sand = Sand((x, y))
                    self.tiles.add(tile_S)
                if cell == "G":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_G: Grass = Grass((x, y))
                    self.tiles.add(tile_G)
                if cell == "F":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_F: Snow_dirt = Snow_dirt((x, y))
                    self.tiles.add(tile_F)
                if cell == "H":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_H: Snow = Snow((x, y))
                    self.tiles.add(tile_H)
                if cell == "M":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_M: melting_snow = melting_snow((x, y))
                    self.tiles.add(tile_M)
                if cell == "W":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_W: water = water((x, y))
                    self.tiles.add(tile_W)
                    self.tiles_dict[(x, y)] = tile_W
                if cell == "B":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_B: water_bottom = water_bottom((x, y))
                    self.tiles.add(tile_B)
                if cell == "D":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_D: melting_dirt = melting_dirt((x, y))
                    self.tiles.add(tile_D)
                if cell == "g":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_g: melting_grass = melting_grass((x, y))
                    self.tiles.add(tile_g)

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



    def check_water_block(self, time: int) -> None:
        player: Player = self.player.sprite
        player_rect = player.rect
        player_rect_bottom_center = player_rect.bottomleft[0] + player_rect.width // 2, player_rect.bottom

        for pos, tile in self.tiles_dict.items():
            if tile.rect.collidepoint(player_rect_bottom_center):
                with open("records.txt", "a", encoding="utf-8") as file:
                    file.write(f"{str(time)}\n")

    def scroll_x(self) -> float:
        player: Player = self.player.sprite
        player_x: int = player.rect.centerx
        direction_x: float = player.direction.x

        if player_x < width / 2 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > width - (width / 2) and direction_x > 0:
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
