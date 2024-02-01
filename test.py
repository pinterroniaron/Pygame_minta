class Level:
    def __init__(
        self, level_data: list[str], surface: pygame.Surface, clouds_group: None
    ):
        self.display_surface: pygame.Surface = surface
        self.setup_level(level_data)
        self.clouds_group = clouds_group
        self.world_shift: int = 0
        self.end_time = None  # Initialize end time as None

    def setup_level(self, layout: list[str]) -> None:
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                # Tile setup code...
                if cell == "W":  # Check for the W block
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_W: water = water((x, y))
                    self.tiles.add(tile_W)

    def check_end_condition(self):
        """Check if the player is on top of the W block at the end of the map."""
        for player_sprite in self.player.sprites():
            player_rect = player_sprite.rect
            for tile in self.tiles:
                if tile.rect.colliderect(player_rect):
                    if tile.type == "W" and player_sprite.rect.bottom == tile.rect.top:
                        self.end_time = pygame.time.get_ticks() / 1000
                        return True
        return False

    def run(self) -> None:
        # Other run methods...

        # Check if the end condition is met
        if self.check_end_condition() and self.end_time is not None:
            print("Player reached the end at time:", self.end_time)
