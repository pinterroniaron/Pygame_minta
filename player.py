from typing import Dict, List

import pygame

from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.import_character_assets()
        self.frame_index: float = 0
        self.status: str = "idle"
        self.animation_speed: float = 0.35
        self.animation_speed_idle: float = 0.05
        self.image = self.animations["idle"][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed: int = 8
        self.gravity: float = 0.6
        self.jump_speed: float = -16
        self.facing_left: bool = True
        self.on_ground: bool = False
        self.on_ceiling: bool = False
        self.on_left: bool = False
        self.on_right: bool = False

    def import_character_assets(self) -> None:
        character_path: str = "graphics/character/"
        self.animations: Dict[str, List[pygame.Surface]] = {
            "idle": [],
            "run": [],
            "jump": [],
            "fall": [],
        }

        for animation in self.animations.keys():
            full_path: str = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self) -> None:
        animation: List[pygame.Surface] = self.animations[self.status]

        if self.status == "idle":
            self.frame_index += self.animation_speed_idle
        else:
            self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            self.frame_index = 0

        image: pygame.Surface = animation[int(self.frame_index)]

        if self.facing_left:
            self.image = image
        else:
            flipped_image: pygame.Surface = pygame.transform.flip(
                image, True, False)
            self.image = flipped_image

    def get_status(self) -> None:
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def get_input(self) -> None:
        keys: List[bool] = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_left = False
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_left = True
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_ground or keys[pygame.K_w] and self.on_ground:
            self.jump()

    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self) -> None:
        self.direction.y = self.jump_speed

    def get_y_position(self) -> int:
        return self.rect.y

    def update(self) -> None:
        self.get_input()
        self.get_status()
        self.animate()
