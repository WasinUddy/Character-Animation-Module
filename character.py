import json
import pygame as pg

class CharacterSprite:
    """
    A class to store the tiles and be queried for the character.
    """
    def __init__(self, path_to_tiles: str, target_size: tuple = (32, 32)):
        """
        Initialize the CharacterTiles instance.

        Args:
            path_to_tiles (str): The path to the tile image path json to be used for rendering.
            target_size (tuple, optional): The target size of the tile images. Defaults to (32, 32).
        """
        self.target_size = target_size
        self.load_tiles(path_to_tiles)    
        self.counter_n = 0
        self.character_state = "idle"

    def load_tiles(self, path_to_tiles: str):
        """
        Load the tiles from the file.

        Args:
            path_to_tiles (str): The path to the tile image path json.
        """
        with open(path_to_tiles, "r") as f:
            data = json.load(f)

        self.tiles = {}
        for key, tile_path_list in data.items():
            self.tiles[key] = []
            for tile_path in tile_path_list:
                tile = pg.image.load(tile_path)
                tile = pg.transform.scale(tile, self.target_size)
                self.tiles[key].append(tile)
        
    def counter_update(self):
        """
        Update the counter of the tiles to be in range of 0-100
        """
        if self.counter_n >= 100:
            self.counter_n = -1
        self.counter_n += 1
        
    def idle(self, direction: str = "S"):
        """
        Return the idle tile of the character.

        Returns:
            pygame.Surface: The idle tile of the character.
        """
        self.counter_update()
        return self.tiles[f"idle_{direction}"][self.counter_n % len(self.tiles[f"idle_{direction}"])]
    
    def walk(self, direction: str):
        """
        Return the walking tile of the character.

        Args:
            direction (str): The direction of the character.

        Returns:
            pygame.Surface: The walking tile of the character.
        """
        self.counter_update()
        return self.tiles[f"walk_{direction}"][self.counter_n % len(self.tiles[f"walk_{direction}"])]




    


