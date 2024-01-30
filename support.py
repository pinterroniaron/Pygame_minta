from os import walk
from typing import List

import pygame


def import_folder(path: str) -> List[pygame.Surface]:
    surface_list: List[pygame.Surface] = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path: str = path + "/" + image
            image_surf: pygame.Surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
