import json
from tiles import Tiles


class GArray:
    """
    Game Array class to handle 2D game events and manipulations before being used for rendering.
    """

    def __init__(self, game_map_file: str):
        """
        Initialize the GArray instance.

        Args:
            game_map_file (str): The file path of the game map to be used for rendering.
        """
        self.load_map(game_map_file)

    def load_map(self, game_map_file: str):
        """
        Load the game map from the file.

        Args:
            game_map_file (str): The file path of the game map.
        """
        with open(game_map_file, "r") as f:
            data = json.load(f)

        gmap = data.get("map", {})
        # tile_paths = data.get("tile_path", {})

        max_x = max_y = 0
        for key in gmap:
            x, y = map(int, key.split(";"))
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        self.width = max_x + 1
        self.height = max_y + 1

        self.data = [[Tiles("VOID") for _ in range(self.width)] for _ in range(self.height)]
        for key, tile_data in gmap.items():
            x, y = map(int, key.split(";"))
            if "0" in tile_data:
                self.data[y][x] = Tiles(tile_data["0"][0])

    def ripple(self, pos: tuple):
        """
        Activate surrounding tiles of the given position in a ripple effect.

        Args:
            pos (tuple): The position of the tile to be activated.
        """
        x, y = pos

        # Activate side function of the surrounding tiles
        if x > 0:
            self.data[y][x - 1].side()
        if x < self.width - 1:
            self.data[y][x + 1].side()
        if y > 0:
            self.data[y - 1][x].side()
        if y < self.height - 1:
            self.data[y + 1][x].side()

        # Activate custom function of the surrounding tiles
        if x > 0:
            self.data[y][x - 1].up()
        if x < self.width - 1:
            self.data[y][x + 1].down()
        if y > 0:
            self.data[y - 1][x].left()
        if y < self.height - 1:
            self.data[y + 1][x].right()

        # Activate custom function of the tile at the given position
        self.data[y][x].here()

    def __str__(self):
        """
        Return the string representation of the game array in a formatted table with summarized data.

        Returns:
            str: The string representation of the game array.
        """
        max_length = max(len(str(tile)) for row in self.data for tile in row)

        table = ""
        for row in self.data:
            table += " ".join(f"{str(tile):<{max_length}}" for tile in row) + "\n"

        return table + f"\nWidth: {self.width}\nHeight: {self.height}"
