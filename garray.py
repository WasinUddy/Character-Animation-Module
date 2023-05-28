import json
from tiles import Tiles

class GArray:
    """
    Game Array class to handle 2D Game events and manipulations before being use for rendering
    """

    def __init__(self, game_map: str):
        """
        Class constructor.

        Args:
            game_map (str): The game map to be used for rendering load from the file
        """
        self.load_map(game_map)    # Load the game map from the file Generate self.data, self.width, self.height

    def load_map(self, game_map: str):
        """
        Load the game map from the file
        
        game_map format
        {
            "map": {
                "x;y": {
                    "0": "tile_type",
                    "1": "tile_type",
                }
            }
            "tile_path": {
                "tile_type": "path/to/tile"
            }
        }
        """

        with open(game_map, "r") as f:
            data = json.load(f)
        
        gmap = data["map"]
        #tils_path = data["tile_path"]

        # Get the size of the map
        # Max X
        max_x, max_y = 0, 0
        for key in gmap.keys():
            x , y = tuple(map(int, key.split(";")))
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        
        self.height = max_y + 1
        self.width = max_x + 1

        # Create the array
        self.data = [[None for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if f"{x};{y}" in gmap.keys():
                    self.data[y][x] = Tiles(gmap[f"{x};{y}"]["0"][0])       # Select only the first layer of the tile will FIX LATER
                else:
                    self.data[y][x] = Tiles("VOID")
        

        


                



if __name__ == "__main__":
    g = GArray("map.json")
    print(g.data)
    print(g.width, g.height)
    print(g.data[0][0   ])