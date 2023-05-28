class Tiles:
    """
    Base class for every tile in the game and can be overridden to create custom tiles to cooperate with the game.
    The tile will be able to interact with characters, e.g., a character on top of the tile may affect the character's speed.
    """

    def __init__(self, tile_type: str):
        """
        Class constructor.

        Args:
            tile_type (str): The type of the tile to be selected for rendering.
        """
        self.tile_type = tile_type

    def up(self):
        """
        The effect of the tile when the character is on top of the tile.
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

    def here(self):
        """
        The effect of the tile when the character is on the tile.
        """
        pass

    def side(self):
        """
        The effect of the tile when the character is on the side of the tile.
        """
        pass

    def __str__(self):
        """
        Return the string representation of the tile.

        Returns:
            str: The string representation of the tile.
        """
        return self.tile_type
    