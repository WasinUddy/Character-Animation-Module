class Tiles:
    """
    Base class for every tile in the game and can be override to create custom tiles to coperate with the game.
    The tile will be able to interact with character eg character on the top of the tile will affect the character's speed.
    """

    def __init__(self, tile_type: str):
        """
        Class constructor.

        Args:
            tile_type (str): The type of the tile to be selected for rendering
        """
        self.tile_type = tile_type

    
    def up(self):
        """
        The effect of the tile when the character is on the top of the tile.
        """
        pass


    def down(self):
        """
        The effect of the tile when the character is on the bottom of the tile.
        """
        pass


    def left(self):
        """
        The effect of the tile when the character is on the left of the tile.
        """
        pass


    def right(self):
        """
        The effect of the tile when the character is on the right of the tile.
        """
        pass

    
    def side(self):
        """
        The effect of the tile when the character is on the side of the tile.
        """
        pass

    def __str__(self):
        return self.tile_type





    
